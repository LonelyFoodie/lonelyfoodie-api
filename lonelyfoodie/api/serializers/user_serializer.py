from flask_restx import fields
from lonelyfoodie.api.restx import api

user = api.model('user', {
    'id': fields.String(readOnly=True),
    'kakao_id': fields.String(readOnly=True),
    'username': fields.String(),
    'email': fields.String(),
    'nickname': fields.String(),
    'dept_code': fields.String(),
    'student_year': fields.String(),
    'sex': fields.String(),
    'created_at': fields.DateTime(),
    'updated_at': fields.DateTime(),
    'deleted_at': fields.DateTime()
})

user_request = api.model('UserCreate', {
    'username': fields.String(),
    'email': fields.String(),
    'nickname': fields.String(),
    'dept_code': fields.String(),
    'student_year': fields.String(),
    'sex': fields.String()
})