import logging

from flask import request
from flask_restx import Resource
from lonelyfoodie.api.services.review_service import ReviewService
from lonelyfoodie.api.serializers.review_serializer import review, review_create_request, review_update_request
from lonelyfoodie.api.parsers import pagination_arguments, review_search_arguments, user_authorization_arguments
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
        per_page = args.get('per_page', 20)

        args = review_search_arguments.parse_args(request)
        title = args.get('title', '')
        content = args.get('content', '')

        if title:
            reviews = service.find_with_title(page, per_page, title)
        elif content:
            reviews = service.find_with_content(page, per_page, content)
        else:
            reviews = service.find()

        return reviews

    @api.expect(review_create_request, user_authorization_arguments)
    @api.response(201, 'Review successfully created.')
    def post(self):
        args = user_authorization_arguments.parse_args(request)
        authorization = args.get('Authorization')

        data = request.json or {}
        service.create(data, authorization)
        return None, 201


@ns.route('/<id>')
@api.response(404, 'Review not found.')
class ReviewItem(Resource):

    @api.marshal_with(review)
    def get(self, id):
        restaurant = service.find_one(id)
        return restaurant

    @api.expect(review_update_request, user_authorization_arguments)
    @api.response(204, 'Review successfully updated.')
    def patch(self, id):
        args = user_authorization_arguments.parse_args(request)
        authorization = args.get('Authorization')

        data = request.json or {}
        service.update(id, data, authorization)
        return None, 204

    @api.expect(user_authorization_arguments)
    @api.response(204, 'Review successfully deleted.')
    def delete(self, id):
        args = user_authorization_arguments.parse_args(request)
        authorization = args.get('Authorization')

        service.remove(id, authorization)
        return None, 204

