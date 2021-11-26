import logging

from flask import request
from flask_restx import Resource
from lonelyfoodie.api.services.user_service import User
from lonelyfoodie.api.serializers.user_serializer import user, user_request
from lonelyfoodie.api.parsers import pagination_arguments, user_search_arguments
from lonelyfoodie.api.restx import api

service_user = User()

log = logging.getLogger(__name__)
ns_user = api.namespace('users', description='Operations related to users')

###user
@ns_user.route('/')
class UserCollection(Resource):

    @api.expect(pagination_arguments, user_search_arguments)
    @api.marshal_list_with(user)
    def get(self):
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        args = user_search_arguments.parse_args(request)
        name = args.get('name', '')

        Users = service_user.find(page, per_page, name)
        return Users

    @api.expect(user_request)
    @api.response(201, 'User successfully created.')
    def post(self):
        data = request.json or {}
        service_user.create(data)
        return None, 201


@ns_user.route('/<id>')
@api.response(404, 'User not found.')
class UsertItem(Resource):

    @api.marshal_with(user)
    def get(self, id):
        user = service_user.find_one(id)
        return user

    @api.expect(user_request)
    @api.response(204, 'User successfully updated.')
    def patch(self, id):
        data = request.json or {}
        service_user.update(id, data)
        return None, 204

    @api.response(204, 'User successfully deleted.')
    def delete(self, id):
        service_user.remove(id)
        return None, 204
