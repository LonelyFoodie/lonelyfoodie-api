from lonelyfoodie.database import Database
from lonelyfoodie.database.models import User
from lonelyfoodie.api.repositories.repository import Repository


class OAuthRepository(Repository):
    def __init__(self):
        self.obj = User
        self.db = None

        with Database() as db:
            self.db = db

        super().__init__(self.obj, self.db)
