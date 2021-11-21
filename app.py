import logging.config

import os
from flask import Flask, Blueprint, render_template, request, jsonify, make_response
from flask_jwt_extended import (
    JWTManager, create_access_token, 
    get_jwt_identity, jwt_required,
    set_access_cookies, set_refresh_cookies, 
    unset_jwt_cookies, create_refresh_token,
    jwt_refresh_token_required,
)
import settings
from lonelyfoodie.api.controllers.restaurant_controller import ns as restaurants_namespace
from lonelyfoodie.api.controllers.Oauth_controller import Oauth
from lonelyfoodie.api.restx import api
from Oauth_model import UserModel, UserData
from config import CLIENT_ID, REDIRECT_URI


app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['JWT_SECRET_KEY'] = "I'M IML."
    flask_app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    flask_app.config['JWT_COOKIE_SECURE'] = False
    flask_app.config['JWT_COOKIE_CSRF_PROTECT'] = True
    flask_app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 30
    flask_app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 100

def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(restaurants_namespace)
    flask_app.register_blueprint(blueprint)


def main():
    initialize_app(app)
    jwt = JWTManager(app)
    @app.route("/login")
    def index():
        return render_template('index.html')


    @app.route("/oauth")
    def oauth_api():
        """
        # OAuth API [GET]
        사용자로부터 authorization code를 인자로 받은 후,
        아래의 과정 수행함
        1. 전달받은 authorization code를 통해서
            access_token, refresh_token을 발급.
        2. access_token을 이용해서, Kakao에서 사용자 식별 정보 획득
        3. 해당 식별 정보를 서비스 DB에 저장 (회원가입)
        3-1. 만약 이미 있을 경우, (3) 과정 스킵
        4. 사용자 식별 id를 바탕으로 서비스 전용 access_token 생성
        """
        code = str(request.args.get('code'))
        
        oauth = Oauth()
        auth_info = oauth.auth(code)
        user = oauth.userinfo("Bearer " + auth_info['access_token'])
        
        """
        user_info = user['kakao_account']['profile']
        self.id = user['id']
        self.nickname = user_info['nickname']
        self.profile = user_info['profile_image_url']
        self.thumbnail = user_info['thumbnail_image_url']
        """

        resp = make_response(render_template('index.html'))
        
        access_token = create_access_token(identity=user['id'])
        refresh_token = create_refresh_token(identity=user['id'])
        resp.set_cookie("logined", "true")
        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)
        
        return resp


    @app.route('/token/refresh')
    @jwt_refresh_token_required
    def token_refresh_api():
        """
        Refresh Token을 이용한 Access Token 재발급
        """
        user_id = get_jwt_identity()
        resp = jsonify({'result': True})
        access_token = create_access_token(identity=user_id)
        set_access_cookies(resp, access_token)
        return resp


    @app.route('/token/remove')
    def token_remove_api():
        """
        Cookie에 등록된 Token 제거
        """
        resp = jsonify({'result': True})
        unset_jwt_cookies(resp)
        resp.delete_cookie('logined')
        return resp

    
    @app.route("/userinfo")
    @jwt_required
    def userinfo():
    
        #Access Token을 이용한 DB에 저장된 사용자 정보 가져오기
    
        user_id = get_jwt_identity()
        userinfo = UserModel().get_user(user_id).serialize()
        return jsonify(userinfo)
    

    @app.route('/oauth/url')
    def oauth_url_api():
        """
        Kakao OAuth URL 가져오기
        """
        return jsonify(
            kakao_oauth_url="https://kauth.kakao.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code" \
            % (CLIENT_ID, REDIRECT_URI)
        )


    @app.route("/oauth/refresh", methods=['POST'])
    def oauth_refesh_api():
        """
        # OAuth Refresh API
        refresh token을 인자로 받은 후,
        kakao에서 access_token 및 refresh_token을 재발급.
        (% refresh token의 경우, 
        유효기간이 1달 이상일 경우 결과에서 제외됨)
        """
        refresh_token = request.get_json()['refresh_token']
        result = Oauth().refresh(refresh_token)
        return jsonify(result)


    @app.route("/oauth/userinfo", methods=['POST'])
    def oauth_userinfo_api():
        """
        # OAuth Userinfo API
        kakao access token을 인자로 받은 후,
        kakao에서 해당 유저의 실제 Userinfo를 가져옴
        """
        access_token = request.get_json()['access_token']
        result = Oauth().userinfo("Bearer " + access_token)
        return jsonify(result)

    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(host='0.0.0.0', port='5000', debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()