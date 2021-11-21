# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

import uuid
import enum

from sqlalchemy import Column, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import Enum

from .base import Base

class sexType(enum.Enum):
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

class Users(Base):
    __tablename__='users'

    id = Column(String(120), primary_key=True, default=lambda: str(uuid.uuid4()))
    username=Column(String(120), nullable=False)
    email=Column(String(120), unique=True ,nullable=False)
    nickname=Column(String(120), unique=True ,nullable=False)
    dept_code=Column(String(120) ,nullable=False)
    student_year=Column(String(120) ,nullable=False)
    #sex=Column(Enum(sexType),nullable=False),
    sex=Column(String(120) ,nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True))

