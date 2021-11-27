import requests

from lonelyfoodie.api.services.service import Service
from lonelyfoodie.api.repositories.user_repository import UserRepository
from lonelyfoodie.api.utils.user import authorize


class UserService(Service):
    def __init__(self):
        self.repository = UserRepository()
        super().__init__(self.repository)

    @authorize
    def find_by_access_token(self, authorization):
        profile = requests.get(
            "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {authorization}"},
        ).json()

        kakao_id = str(profile['id'])

        return self.repository.find_by_kakao_id(kakao_id)

    @authorize
    def find_one(self, id):
        return super().find_one(id)

    @authorize
    def update(self, id, data):
        super().update(id, data)

    @authorize
    def remove(self, id):
        super().remove(id)
