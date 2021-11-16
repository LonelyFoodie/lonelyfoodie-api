from werkzeug.exceptions import NotFound
from lonelyfoodie.database import use_database
from lonelyfoodie.database.models import Restaurant


@use_database
def create(db, data):
    restaurant = Restaurant()

    for key, value in data.items():
        setattr(restaurant, key, value)

    db.add(restaurant)
    db.commit()


@use_database
def find_one(db, restaurant_id):
    restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).one()
    if not restaurant:
        raise NotFound()
    return restaurant


@use_database
def find(db, page, per_page, name):
    query = db.query(Restaurant)

    if name:
        query = query.filter(Restaurant.name.like(f'%{name}%'))

    restaurants = query.offset((page - 1) * per_page).limit(per_page).all()

    return restaurants


@use_database
def update(db, restaurant_id, data):
    restaurant = find_one(restaurant_id)

    for key, value in data.items():
        setattr(restaurant, key, value)

    db.add(restaurant)
    db.commit()


@use_database
def remove(db, restaurant_id):
    restaurant = find_one(restaurant_id)
    db.delete(restaurant)
    db.commit()
