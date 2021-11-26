from lonelyfoodie.api.services.service import Service
from lonelyfoodie.api.repositories.oauth_repository import OAuthRepository
 

class UserService(Service):
    def __init__(self):
        self.repository = OAuthRepository()
        super().__init__(self.repository)

    def create(self, data):
        nickname = data['properties']['nickname']
        kakao_id = str(data['id'])
        email = data['kakao_account']['email']

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
        
