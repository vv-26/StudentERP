from sqlalchemy import Column, Integer, String,Date
from database import Base

class Student(Base):
    __tablename__ = "students"
    stuid = Column(Integer, primary_key = True)
    name = Column(String)
    dept = Column(String)
    program = Column(String)
    DOB = Column(Date)
    batch = Column(String)
    email = Column(String, unique = True)

