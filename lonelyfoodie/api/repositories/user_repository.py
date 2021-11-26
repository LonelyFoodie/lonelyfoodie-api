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

    def find_with_nickname(self, page, per_page, nickname):
        query = self.db.query(User)

        if nickname:
            query = query.filter(User.nickname.like(f'%{nickname}%'))

        users = query.offset((page - 1) * per_page).limit(per_page).all()

        return users

