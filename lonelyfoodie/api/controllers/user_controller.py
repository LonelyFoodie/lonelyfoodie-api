import logging

from flask import request
from flask_restx import Resource
from lonelyfoodie.api.services.user_service import UserService
from lonelyfoodie.api.serializers.user_serializer import user, user_request
from lonelyfoodie.api.parsers import user_authorization_arguments
from lonelyfoodie.api.restx import api

service = UserService()

log = logging.getLogger(__name__)
ns = api.namespace('users', description='Operations related to users')


@ns.route('/')
@api.response(400, 'Authorization header is not present.')
@api.response(401, 'Access token is not valid.')
class UserCollection(Resource):

    @api.expect(user_authorization_arguments)
    @api.marshal_list_with(user)
    def get(self):
        user_authorization_arguments.parse_args(request)
        authorization = user_authorization_arguments.get('Authorization')

        user = service.find_by_access_token(authorization)
        return user, 200


@ns.route('/<id>')
@api.expect(user_authorization_arguments)
@api.response(400, 'Authorization header is not present.')
@api.response(401, 'Access token is not valid.')
@api.response(404, 'User not found.')
class UserItem(Resource):
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
