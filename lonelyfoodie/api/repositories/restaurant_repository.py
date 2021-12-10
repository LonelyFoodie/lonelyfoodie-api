from werkzeug.exceptions import NotFound

from sqlalchemy.sql import func
from lonelyfoodie.api.repositories.repository import Repository
from lonelyfoodie.database import use_database, Database
from lonelyfoodie.database.models import Restaurant, Review


class RestaurantRepository(Repository):
    def __init__(self):
        self.obj = Restaurant
        self.db = None

        with Database() as db:
            self.db = db

        super().__init__(self.obj, self.db)

    def find_with_review(self, id):
        restaurant = self.find_one(id)
        review_count = self.db.query(Review)\
            .filter(Review.restaurant_id == restaurant.id) \
            .count()
        avg_star_rate = self.db.query(func.avg(Review.star)) \
            .filter(Review.restaurant_id == restaurant.id) \
            .one()
        avg_star_rate = avg_star_rate[0]

        return {
         'restaurant': restaurant,
         'review_count': review_count,
         'avg_star_rate': avg_star_rate
        }

    def find_with_argument(self, page, per_page, name):
        query = self.db.query(Restaurant)

        if name:
            query = query.filter(Restaurant.name.like(f'%{name}%'))

        restaurants = query.offset((page - 1) * per_page).limit(per_page).all()

        return restaurants

    def find_with_kakaomap_id(self, id):
        restaurant = self.db.query(Restaurant) \
            .filter(Restaurant.kakaomap_id == id) \
            .first()

        if not restaurant:
            raise NotFound

        review_count = self.db.query(Review) \
            .filter(Review.restaurant_id == restaurant.id) \
            .count()
        avg_star_rate = self.db.query(func.avg(Review.star)) \
            .filter(Review.restaurant_id == restaurant.id) \
            .one()

        avg_star_rate = avg_star_rate[0]

        return {
         'restaurant': restaurant,
         'review_count': review_count,
         'avg_star_rate': avg_star_rate
        }
