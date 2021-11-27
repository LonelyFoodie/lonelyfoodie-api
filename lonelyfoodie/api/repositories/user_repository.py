from lonelyfoodie.database import Database
from lonelyfoodie.database.models import User
from lonelyfoodie.api.repositories.repository import Repository


class UserRepository(Repository):
    def __init__(self):
        self.obj = User
        self.db = None

        with Database() as db:
            self.db = db

        super().__init__(self.obj, self.db)

    def find_by_kakao_id(self, kakao_id: str):
        user = self.db.query(User) \
            .filter(User.kakao_id == kakao_id,
                    User.deleted_at.is_(None)) \
            .first()

        return user


