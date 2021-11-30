import logging

from flask import request
from flask_restx import Resource
from lonelyfoodie.api.services.review_service import ReviewService
from lonelyfoodie.api.serializers.review_serializer import review, review_request
from lonelyfoodie.api.parsers import pagination_arguments, review_search_arguments, review_search_arguments2
from lonelyfoodie.api.restx import api

service = ReviewService()

log = logging.getLogger(__name__)

ns = api.namespace('review', description='Operations related to review')


@ns.route('/')
class ReviewCollection(Resource):

    @api.expect(pagination_arguments, review_search_arguments)
    @api.marshal_list_with(review)
    def get(self):
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        args = review_search_arguments.parse_args(request)
        keyword = args.get('name', '')

        reviews = service.find_with_title(page, per_page, keyword)
        return reviews

    @api.expect(review_request)
    @api.response(201, 'Review successfully created.')
    def post(self):
        data = request.json or {}
        service.create(data)
        return None, 201


@ns.route('/<id>')
@api.response(404, 'Review not found.')
class ReviewItem(Resource):

    @api.marshal_with(review)
    def get(self, id):
        restaurant = service.find_one(id)
        return restaurant

    @api.expect(review_request)
    @api.response(204, 'Review successfully updated.')
    def patch(self, id):
        data = request.json or {}
        service.update(id, data)
        return None, 204

    @api.response(204, 'Review successfully deleted.')
    def delete(self, id):
        service.remove(id)
        return None, 204

