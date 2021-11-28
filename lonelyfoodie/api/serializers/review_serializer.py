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

review_request = api.model('ReviewCreate', {
    'title': fields.String(),
    'content': fields.String(),
    'star': fields.Integer()
})