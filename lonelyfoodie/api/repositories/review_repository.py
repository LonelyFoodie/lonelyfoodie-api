from werkzeug.exceptions import NotFound
from lonelyfoodie.api.repositories.repository import Repository
from lonelyfoodie.database import use_database, Database
from lonelyfoodie.database.models import Review


class ReviewRepository(Repository):
    def __init__(self):
        self.obj = Review
        self.db = None

        with Database() as db:
            self.db = db

        super().__init__(self.obj, self.db)

    def find_with_title(self, page, per_page, keyword):
        query = self.db.query(Review)

        if keyword:
            query = query.filter(Review.title.like(f'%{keyword}%'))

        review = query.offset((page - 1) * per_page).limit(per_page).all()

        return review

    def find_with_content(self, page, per_page, keyword):
        query = self.db.query(Review)

        if keyword:
            query = query.filter(Review.content.like(f'%{keyword}%'))

        review = query.offset((page - 1) * per_page).limit(per_page).all()

        return review
