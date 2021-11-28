from lonelyfoodie.api.services.service import Service
from lonelyfoodie.api.repositories.review_repository import ReviewRepository


class ReviewService(Service):
    def __init__(self):
        self.repository = ReviewRepository()
        super().__init__(self.repository)

    def find_with_title(self, page, per_page, keyword):
        review = self.repository.find_with_title(page, per_page, keyword)
        return review

    def find_with_content(self, page, per_page, keyword):
        review = self.repository.find_with_content(page, per_page, keyword)
        return review