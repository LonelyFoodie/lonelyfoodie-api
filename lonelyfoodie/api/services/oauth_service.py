from flask import request, redirect
from sqlalchemy.sql.expression import null
import lonelyfoodie.api.repositories.oauth_repository as repository
 

class User:
    def social_signup(data):
        kakao_properties = data.get("properties")
        kakao_accounts = data.get("kakao_account")
        nickname = kakao_properties.get("nickname")
        kakao_id = str(data.get("id"))
        email = kakao_accounts.get("email")
        setup_data = {
            'kakao_id':kakao_id,
            'username': nickname,
            'email': email,
            'nickname': "null",
            'dept_code': "null",
            'student_year': "null",
            'sex':"null"
        }
        repository.create(setup_data)
        
