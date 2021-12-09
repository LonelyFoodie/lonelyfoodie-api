from flask_restx import fields
from lonelyfoodie.api.restx import api

restaurant = api.model('Restaurant', {
    'id': fields.String(readOnly=True),
    'name': fields.String(),
    'kakaomap_id': fields.String(),
    'reviews': fields.String(),
    'rating_avg': fields.Float(),
    'latitude': fields.Float(),
    'longitude': fields.Float(),
    'created_at': fields.DateTime(),
    'updated_at': fields.DateTime(),
    'deleted_at': fields.DateTime()
})

restaurant_request = api.model('RestaurantCreate', {
    'name': fields.String(),
    'kakaomap_id': fields.String(),
    'reviews': fields.String(),
    'rating_avg': fields.Float(),
    'latitude': fields.Float(),
    'longitude': fields.Float()
})