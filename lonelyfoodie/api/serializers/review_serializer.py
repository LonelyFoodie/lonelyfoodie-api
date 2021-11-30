from flask_restx import fields
from lonelyfoodie.api.restx import api

review = api.model('Review', {
    'id': fields.String(readOnly=True),
    'restaurant_id': fields.String(readOnly=True),
    'writer_id': fields.String(readOnly=True),
    'title': fields.String(),
    'content': fields.String(),
    'star': fields.Integer(),
    'created_at': fields.DateTime(),
    'updated_at': fields.DateTime(),
    'deleted_at': fields.DateTime()
})

review_create_request = api.model('ReviewCreateRequest', {
    'restaurant_id': fields.String(readOnly=True, required=True),
    'title': fields.String(required=True),
    'content': fields.String(required=True),
    'star': fields.Integer(),
})

review_update_request = api.model('ReviewUpdateCreate', {
    'title': fields.String(),
    'content': fields.String(),
    'star': fields.Integer()
})