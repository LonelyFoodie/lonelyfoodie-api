import logging
import traceback

from flask_restx import Api
import settings
from sqlalchemy.orm.exc import NoResultFound

log = logging.getLogger(__name__)

api = Api(version='2.0', title='Lonely Foodie API',
          description='고독한 시식가 프로젝트 서버의 API입니다.\n <a href="http://localhost:5000/login" target="blank">로그인 예제</a>')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    """No results found in database"""
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404

