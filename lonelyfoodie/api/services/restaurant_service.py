from lonelyfoodie.api.services.service import Service
from lonelyfoodie.api.repositories.restaurant_repository import RestaurantRepository


class RestaurantService(Service):
    def __init__(self):
        self.repository = RestaurantRepository()
        super().__init__(self.repository)

    def find_with_argument(self, page, per_page, name):
        restaurants = self.repository.find_with_argument(page, per_page, name)
        return restaurants

    def find_one_by_kakaomap_id(self, kakaomap_id):
        restauransts = self.repository.find_one_by_kakaomap_id(kakaomap_id)
        return restauransts