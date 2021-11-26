from lonelyfoodie.api.services.service import Service
from lonelyfoodie.api.repositories.restaurant_repository import RestaurantRepository


class RestaurantService(Service):
    def __init__(self):
        self.repository = RestaurantRepository()
        super().__init__(self.repository)

    def find_with_argument(self, page, per_page, name):
        restaurants = self.repository.find_with_argument(page, per_page, name)
        return restaurants