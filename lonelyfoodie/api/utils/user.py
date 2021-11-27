import requests

from flask import request
from werkzeug.exceptions import Unauthorized, BadRequest
from functools import wraps

from lonelyfoodie.database import Database
from lonelyfoodie.database.models import User


def authorize(f):
    @wraps(f)
    def deco(self, *args, **kwargs):
        access_token = request.headers.get('Authorization')
        if not access_token:
            raise BadRequest('Authorization header is not present.')

        profile = requests.get(
            "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"},
        ).json()

        if 'id' not in profile:
            raise Unauthorized('Access token is not valid.')

        kakao_id = str(profile['id'])

        with Database() as db:
            user = db.query(User) \
                .filter(User.kakao_id == kakao_id,
                        User.deleted_at.is_(None)) \
                .first()

            if not user:
                raise Unauthorized('User does not exist.')
        return f(self, *args, **kwargs)

    return deco
