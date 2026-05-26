from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    name: str
    dept: str
    program: str
    DOB: date
    batch: str
    email: EmailStr



class StudentResponse(BaseModel):
    stuid: int
    name: str
    dept: str
    program: str
    DOB: date
    batch: str
    email: EmailStr

    class Config:
        from_attributes = True
    
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    dept: Optional[str] = None
    program: Optional[str] = None
    batch: Optional[str] = None
    DOB: Optional[date] = None