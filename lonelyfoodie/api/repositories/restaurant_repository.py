from sqlalchemy.sql.functions import count
from werkzeug.exceptions import NotFound
from lonelyfoodie.api.repositories.repository import Repository
from lonelyfoodie.database import use_database, Database
from lonelyfoodie.database.models import Restaurant
import sys

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

    def update_number_of_reviews_and_raiting(self, data, state):
        if state == "create":
            restaurant_id = data["restaurant_id"]
            star_input = data["star"]
            restaurant = self.find_one(restaurant_id)
            count_temp = restaurant.reviews
            star_temp = restaurant.rating_avg
            
            if count_temp and count_temp != 0:
                star_temp = star_temp * count_temp;
                star_temp += star_input
                count_temp += 1
                star_temp = float(star_temp) / count_temp 
            else:
                count_temp = 1 
                star_temp = star_input

            data = {
                    "reviews" :count_temp,
                    "rating_avg":star_temp
                }
            self.update(restaurant_id,data)


        elif state =="remove":
            review = data
            if review:
                restaurant_id = review.restaurant_id
                review_star = review.star
                restaurant = self.find_one(restaurant_id)
                if restaurant:
                    restaurant_reviews = restaurant.reviews
                    restaurant_star = restaurant.rating_avg

                    star_temp = (restaurant_star * restaurant_reviews) - review_star
                    count_temp = restaurant_reviews - 1
                    if count_temp == 0:
                        count_temp+=1

                    star_temp = star_temp / count_temp

                    data = {
                        "reviews" :count_temp,
                        "rating_avg":star_temp
                    }
                    self.update(restaurant_id,data)


        return restaurant