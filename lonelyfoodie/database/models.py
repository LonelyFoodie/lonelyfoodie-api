# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

import uuid

from sqlalchemy import Column, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func

from .base import Base


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


class Post(Base):
    __tablename__ = 'posts'

    id = Column(String(120), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(80))
    body = Column(String(2000))
    pub_date = Column(DateTime())

    category_id = Column(String, ForeignKey('categories.id'))
    category = relationship('Category', backref=backref('posts', order_by=id))


class Category(Base):
    __tablename__ = 'categories'

    id = Column(String(120), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(50))
