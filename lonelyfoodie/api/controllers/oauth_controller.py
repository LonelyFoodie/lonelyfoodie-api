import logging
import requests

from werkzeug.exceptions import Unauthorized

from flask import redirect
from flask_restx import Resource

from config import CLIENT_ID, REDIRECT_URI, CLIENT_SECRET
from lonelyfoodie.api.restx import api
from lonelyfoodie.api.parsers import kakao_authorization_arguments
from lonelyfoodie.api.services.oauth_service import UserService

log = logging.getLogger(__name__)
ns = api.namespace('oauth', description='Operations related to users')
service = UserService()


@ns.route('/')
class KakaoSignIn(Resource):
    def get(self):
        client_id = CLIENT_ID
        redirect_uri = REDIRECT_URI
        kakao_oauthurl = f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        return redirect(kakao_oauthurl)


@ns.route("/callback/")
class KakaoSignInCallback(Resource):

    @api.expect(kakao_authorization_arguments)
    @api.response(201, 'Successfully registered')
    @api.response(401, 'Invalid Code')
    def get(self):
        args = kakao_authorization_arguments.parse_args()
        code = args.get('code')

        token_response = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&code={code}&client_secret={CLIENT_SECRET}"
        ).json()

        if 'error' in token_response:
            raise Unauthorized(token_response['error'])

        access_token = token_response.get("access_token") #카카오 소셜로그인을 통해 유저에 대한 정보를 받을 권한이 있는 토큰이 이것입니다.
        # 여기까지가 access token 받아오는 통신
        # 그리고 아래 코드가 access tokent 기반으로 유저 정보 요청하는 통신
        profile = requests.get(
                "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"},
        ).json()

        service.create(data=profile)

        return None, 201
