from sqlalchemy import Column, Integer, String,Boolean
from app.database import Base
#creating table into the database
class Student(Base):
    __tablename__="students"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100),nullable=False)
    age=Column(Integer,nullable=False)
    course=Column(String(100),nullable=False)
#creating table for authentication
class users(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(50),unique=True,nullable=False,index=True)
    email=Column(String(100),nullable=False,unique=True,index=True)
    hashed_password=Column(String,nullable=False)
    is_active=Column(Boolean,default=True)
    role=Column(String(50),default="user")