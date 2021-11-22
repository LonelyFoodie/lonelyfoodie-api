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


