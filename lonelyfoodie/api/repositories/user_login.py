from werkzeug.exceptions import NotFound
from lonelyfoodie.database import use_database
from lonelyfoodie.database.models import User


@use_database
def check_log(db,id):
    user = db.query(User).filter(User.id == id).one() # 로그인 할 때 카카오에서 받는 고유 아이디
    if not user:
        raise NotFound()
    return user.id # 로그인 시 유저 id를 넘겨줘서 즐겨찾기, 리뷰 목록 검색 가능하도록