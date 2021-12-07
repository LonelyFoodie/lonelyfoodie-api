# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

import uuid
import enum

from sqlalchemy import Column, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import Enum, Integer

from .base import Base


class SexEnum(enum.Enum):
    male = "male"
    female = "female"


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(String(120), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(120), nullable=False)
    kakaomap_id = Column(String(120), nullable=True)
    latitude = Column(Float(), nullable=True)
    longitude = Column(Float(), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True))


class User(Base):
    __tablename__='users'

    id = Column(String(120), primary_key=True, default=lambda: str(uuid.uuid4()))
    kakao_id = Column(String(120), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    nickname = Column(String(120), nullable=False)
    dept_code = Column(String(120))
    student_year = Column(String(120))
    sex = Column(Enum(SexEnum))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True))

class Review(Base):
    __tablename__='review'

    id = Column(String(120), primary_key=True, default=lambda: str(uuid.uuid4()))
    restaurant_id = Column(String(120), ForeignKey('restaurants.id'), default=lambda: str(uuid.uuid4()))
    writer_id = Column(String(120), ForeignKey('users.id'), default=lambda: str(uuid.uuid4()))
    title = Column(String(120), nullable=False)
    content = Column(String(120), nullable=False)
    star = Column(Integer(), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True))
