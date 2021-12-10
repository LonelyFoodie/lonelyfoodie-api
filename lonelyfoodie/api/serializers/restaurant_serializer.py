from flask_restx import fields
from lonelyfoodie.api.restx import api

restaurant = api.model('Restaurant', {
    'id': fields.String(readOnly=True),
    'name': fields.String(),
    'kakaomap_id': fields.String(),
    'latitude': fields.Float(),
    'longitude': fields.Float(),
    'created_at': fields.DateTime(),
    'updated_at': fields.DateTime(),
    'deleted_at': fields.DateTime()
})

restaurant_with_review = api.model('RestaurantWithReview', {
    'restaurant': fields.Nested(restaurant, skip_none=False),
    'review_count': fields.Integer(),
    'avg_star_rate': fields.Float(),
})

restaurant_request = api.model('RestaurantCreate', {
    'name': fields.String(),
    'kakaomap_id': fields.String(),
    'latitude': fields.Float(),
    'longitude': fields.Float()
})