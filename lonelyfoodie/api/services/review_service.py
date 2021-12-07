from werkzeug.exceptions import Forbidden

from lonelyfoodie.api.services.service import Service
from lonelyfoodie.api.services.user_service import UserService
from lonelyfoodie.api.repositories.review_repository import ReviewRepository
from lonelyfoodie.api.utils.user import authorize


class ReviewService(Service):
    def __init__(self):
        self.repository = ReviewRepository()
        self.user_service = UserService()
        super().__init__(self.repository)

    def is_writer(self, review_id, user_id):
        review = self.repository.find_one(review_id)
        if review.writer_id != user_id:
            return False
        return True

    @authorize
    def create(self, data, authorization):
        user = self.user_service.find_by_access_token(authorization)
        data['writer_id'] = user.id

        return super().create(data)

    @authorize
    def update(self, id, data, authorization):
        user = self.user_service.find_by_access_token(authorization)
        if not self.is_writer(id, user.id):
            raise Forbidden

        return super().update(id, data)

    @authorize
    def remove(self, id, authorization):
        user = self.user_service.find_by_access_token(authorization)
        if not self.is_writer(id, user.id):
            raise Forbidden

        return super().remove(id)

    def find_with_title(self, page, per_page, keyword):
        review = self.repository.find_with_title(page, per_page, keyword)
        return review

    def find_with_content(self, page, per_page, keyword):
        review = self.repository.find_with_content(page, per_page, keyword)
        return review

    def find_with_writer_id(self, page, per_page, writer_id):
        review = self.repository.find_with_writer_id(page, per_page, writer_id)
        return review

    def find_with_restaurant_id(self, page, per_page, restaurant_id):
        review = self.repository.find_with_restaurant_id(page, per_page, restaurant_id)
        return review
        