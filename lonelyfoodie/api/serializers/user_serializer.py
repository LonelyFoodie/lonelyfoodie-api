from flask_restx import fields
from lonelyfoodie.api.restx import api
from lonelyfoodie.database.models import SexEnum


class Sex(fields.Raw):
    def format(self, value):
        if value == SexEnum.female:
            return "female"
        elif value == SexEnum.male:
            return "male"


user_access_token = api.model('AccessToken', {
    'access_token': fields.String(readOnly=True),
})

user = api.model('User', {
    'id': fields.String(readOnly=True),
    'kakao_id': fields.String(readOnly=True),
    'email': fields.String(),
    'nickname': fields.String(),
    'dept_code': fields.String(),
    'student_year': fields.String(),
    'sex': Sex(attribute='sex'),
    'created_at': fields.DateTime(),
    'updated_at': fields.DateTime(),
    'deleted_at': fields.DateTime()
})

user_request = api.model('UserCreate', {
    'email': fields.String(),
    'nickname': fields.String(),
    'dept_code': fields.String(),
    'student_year': fields.String(),
    'sex': fields.String()
})