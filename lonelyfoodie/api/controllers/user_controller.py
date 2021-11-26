import logging

from flask import request
from flask_restx import Resource
from lonelyfoodie.api.services.user_service import UserService
from lonelyfoodie.api.serializers.user_serializer import user, user_request
from lonelyfoodie.api.parsers import pagination_arguments, user_search_arguments
from lonelyfoodie.api.restx import api

service = UserService()

log = logging.getLogger(__name__)
ns = api.namespace('users', description='Operations related to users')


@ns.route('/')
class UserCollection(Resource):

    @api.expect(pagination_arguments, user_search_arguments)
    @api.marshal_list_with(user)
    def get(self):
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        args = user_search_arguments.parse_args(request)
        nickname = args.get('nickname', '')

        users = service.find_with_nickname(page, per_page, nickname)
        return users, 200


@ns.route('/<id>')
@api.response(404, 'User not found.')
class UserItem(Resource):

    @api.marshal_with(user)
    def get(self, id):
        user = service.find_one(id)
        return user

    @api.expect(user_request)
    @api.response(204, 'User successfully updated.')
    def patch(self, id):
        data = request.json or {}
        service.update(id, data)
        return None, 204

    @api.response(204, 'User successfully deleted.')
    def delete(self, id):
        service.remove(id)
        return None, 204
