from lonelyfoodie.api.services.service import Service
from lonelyfoodie.api.repositories.user_repository import UserRepository


class UserService(Service):
    def __init__(self):
        self.repository = UserRepository()
        super().__init__(self.repository)

    def find_with_nickname(self, page, per_page, nickname):
        return self.repository.find_with_nickname(page, per_page, nickname)
