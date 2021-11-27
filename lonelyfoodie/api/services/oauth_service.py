from werkzeug.exceptions import Conflict

from lonelyfoodie.api.services.service import Service
from lonelyfoodie.api.repositories.user_repository import UserRepository
 

class UserService(Service):
    def __init__(self):
        self.repository = UserRepository()
        super().__init__(self.repository)

    def create(self, data):
        nickname = data['properties']['nickname']
        kakao_id = str(data['id'])
        email = data['kakao_account']['email']

        duplicated_user = self.repository.find_by_kakao_id(kakao_id)

        if duplicated_user:
            return 200

        setup_data = {
            'kakao_id': kakao_id,
            'username': nickname,
            'email': email,
            'nickname': nickname,
            'dept_code': None,
            'student_year': None,
            'sex': None
        }
        super().create(setup_data)
        return 201
        
