import lonelyfoodie.api.repositories.user_repository as repository


class User:
    def create(self, data):
        repository.create(data)

    def find_one(self, user_nickname):
        users = repository.find_one(user_nickname)
        return users

    def find(self, page, per_page, name):
        user = repository.find(page, per_page, name)
        return user

    def update(self, user_nickname, data):
        repository.update(user_nickname, data)

    def remove(self, user_nickname):
        repository.remove(user_nickname)