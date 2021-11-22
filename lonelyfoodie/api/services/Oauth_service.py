from flask import request, redirect
import lonelyfoodie.api.repositories.oauth_repository as repository
 

class User:
    def social_signin(data):
        kakao_properties = data.get("properties")
        kakao_accounts = data.get("kakao_account")
        nickname = kakao_properties.get("nickname")
        kakao_id = str(data.get("id"))
        email = kakao_accounts.get("email")
        setup_data = {
            'username': kakao_id,
            'email': email,
            'nickname': nickname,
            'dept_code': "need to be modified",
            'student_year': "need to be modified",
            'sex': "need to be modified"
        }
        repository.create(setup_data)
        
