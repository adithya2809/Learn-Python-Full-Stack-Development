from pydantic import BaseModel
from typing import Optional


class StudentCreate(BaseModel):
    name: str
    age: int
    branch: str
    stats: str
#PATCH PUT
class StudentUpdate(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    branch:Optional[str]=None
    stats:Optional[str]=None
#GET 
class StudentResponse(BaseModel):
    id:int
    name:str
    age:int
    branch:str
    stats:str