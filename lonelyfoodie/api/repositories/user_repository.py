from werkzeug.exceptions import NotFound
from lonelyfoodie.database import use_database
from lonelyfoodie.database.models import Users


@use_database
def create(db, data):
    user = Users()

    for key, value in data.items():
        setattr(user, key, value)

    db.add(user)
    db.commit()


@use_database
def find_one(db, user_id):
    user = db.query(Users).filter(Users.id == user_id).one()
    if not user:
        raise NotFound()
    return user


@use_database
def find(db, page, per_page, name):
    query = db.query(Users)

    if name:
        query = query.filter(Users.nickname.like(f'%{name}%'))

    user = query.offset((page - 1) * per_page).limit(per_page).all()

    return user


@use_database
def update(db, user_id, data):
    user= find_one(user_id)

    for key, value in data.items():
        setattr(user, key, value)

    db.add(user)
    db.commit()


@use_database
def remove(db, user_id):
    user = find_one(user_id)
    db.delete(user)
    db.commit()
