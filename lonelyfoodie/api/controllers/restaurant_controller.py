import logging

from flask import request
from flask_restx import Resource
from lonelyfoodie.api.services.restaurant_service import RestaurantService
from lonelyfoodie.api.serializers.restaurant_serializer import restaurant, restaurant_request, restaurant_with_review
from lonelyfoodie.api.parsers import pagination_arguments, restaurant_search_arguments
from lonelyfoodie.api.restx import api

service = RestaurantService()

log = logging.getLogger(__name__)

ns = api.namespace('restaurants', description='Operations related to restaurants')


@ns.route('/')
class RestaurantCollection(Resource):

    @api.expect(pagination_arguments, restaurant_search_arguments)
    @api.marshal_list_with(restaurant)
    def get(self):
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        name = args.get('name', '')
        restaurants = service.find_with_argument(page, per_page, name)
        return restaurants

    @api.expect(restaurant_request)
    @api.response(201, 'Restaurant successfully created.')
    def post(self):
        data = request.json or {}
        service.create(data)
        return None, 201


@ns.route('/<id>')
@api.response(404, 'Restaurant not found.')
class RestaurantItem(Resource):

    @api.marshal_with(restaurant_with_review)
    def get(self, id):
        restaurant = service.find_with_review(id)
        return restaurant

    @api.expect(restaurant_request)
    @api.response(204, 'Restaurant successfully updated.')
    def patch(self, id):
        data = request.json or {}
        service.update(id, data)
        return None, 204

    @api.response(204, 'Restaurant successfully deleted.')
    def delete(self, id):
        service.remove(id)
        return None, 204


@ns.route('/kakao/<id>')
@api.response(404, 'Restaurant not found.')
class KakaoRestaurantItem(Resource):

    @api.marshal_with(restaurant_with_review)
    def get(self, id):
        restaurant = service.find_with_kakaomap_id(id)
        return restaurant
