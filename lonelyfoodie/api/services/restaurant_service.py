from lonelyfoodie.api.services.service import Service
from lonelyfoodie.api.repositories.restaurant_repository import RestaurantRepository


class RestaurantService(Service):
    def __init__(self):
        self.repository = RestaurantRepository()
        super().__init__(self.repository)

    def find_with_review(self, id):
        restaurants = self.repository.find_with_review(id)
        return restaurants

    def find_with_argument(self, page, per_page, name):
        restaurants = self.repository.find_with_argument(page, per_page, name)
        return restaurants

    def find_with_kakaomap_id(self, id):
        restaurant = self.repository.find_with_kakaomap_id(id)
        return restaurant
