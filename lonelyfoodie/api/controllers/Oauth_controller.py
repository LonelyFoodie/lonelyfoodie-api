import logging
import requests
from flask import request,redirect,make_response
from flask_restx import Resource
from lonelyfoodie.api.restx import api
from config import  CLIENT_ID,REDIRECT_URI,CLIENT_SECRET
from lonelyfoodie.api.services.Oauth_service import User
log = logging.getLogger(__name__)
ns_Oauth = api.namespace('oauth', description='Operations related to users')

@ns_Oauth.route('/')
class KakaoSignIn(Resource):
    def get(self):
        client_id = CLIENT_ID
        redirect_uri = REDIRECT_URI
        kakao_oauthurl = f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        return redirect(kakao_oauthurl)


@ns_Oauth.route("/callback/")
class KakaoSignInCallback(Resource):
    @api.expect()
    @api.response(201, 'kakao Oauth')
    def get(self):
        try:
            code = request.args.get("code")  # callback 뒤에 붙어오는 request token을 뽑아내 줍니다.                                    
            client_id = CLIENT_ID
            redirect_uri = REDIRECT_URI
            client_secret = CLIENT_SECRET
            #Python에서 HTTP 요청을 보내는 모듈인 requests
            token_request = requests.get(                                       
                f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}&client_secret={client_secret}"
            )
            token_json = token_request.json()  # 위의 get 요청을 통해 받아온 데이터를 json화 해주면 이곳에 access token 이 숨어있습니다.
            error = token_json.get("error",None)
            if error is not None :
                return make_response({"message": "INVALID_CODE"}, 400) #에러 처리 한번 해주고
            access_token = token_json.get("access_token") #카카오 소셜로그인을 통해 유저에 대한 정보를 받을 권한이 있는 토큰이 이것입니다. 
            # 여기까지가 access token 받아오는 통신                    
            # 그리고 아래 코드가 access tokent 기반으로 유저 정보 요청하는 통신
            profile_request = requests.get(
                    "https://kapi.kakao.com/v2/user/me", headers={"Authorization" : f"Bearer {access_token}"},
                )
            data = profile_request.json()
        except KeyError:
            return make_response({"message" : "INVALID_TOKEN"}, 400)
 
        except access_token.DoesNotExist:
            return make_response({"message" : "INVALID_TOKEN"}, 400)

        #after this need to 
        User.social_signin(data=data)
        #return redirect('나머지를 입력하는 페이지')
        return None,201
