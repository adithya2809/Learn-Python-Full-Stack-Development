from pydantic import BaseModel
from typing import Optional


class StudentCreate(BaseModel):
    name: str
    age: int
    course: str
#PATCH PUT
class StudentUpdate(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    course:Optional[str]=None
#GET 
class StudentResponse(BaseModel):
    id:int
    name:str
    age:int
    course: str

class Config():  
    from_attributes=True  