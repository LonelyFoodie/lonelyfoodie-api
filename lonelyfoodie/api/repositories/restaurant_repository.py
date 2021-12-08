from werkzeug.exceptions import NotFound
from lonelyfoodie.api.repositories.repository import Repository
from lonelyfoodie.database import use_database, Database
from lonelyfoodie.database.models import Restaurant


class RestaurantRepository(Repository):
    def __init__(self):
        self.obj = Restaurant
        self.db = None

        with Database() as db:
            self.db = db

        super().__init__(self.obj, self.db)

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

        return restaurant
