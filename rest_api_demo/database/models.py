# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

import uuid

from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from .base import Base


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
