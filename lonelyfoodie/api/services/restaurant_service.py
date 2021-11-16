import lonelyfoodie.api.repositories.restaurant_repository as repository


class Restaurant:
    def create(self, data):
        repository.create(data)

    def find_one(self, restaurant_id):
        restaurant = repository.find_one(restaurant_id)
        return restaurant

    def find(self, page, per_page, name):
        restaurants = repository.find(page, per_page, name)
        return restaurants

    def update(self, restaurant_id, data):
        repository.update(restaurant_id, data)

    def remove(self, restaurant_id):
        repository.remove(restaurant_id)