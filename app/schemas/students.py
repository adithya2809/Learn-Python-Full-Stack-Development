from pydantic import BaseModel
from typing import Optional

#POST
class StudentCreate(BaseModel):
    name: str
    age: int
    course: str
#PUT
class StudentUpdate(BaseModel):
    name:str
    age: int
    course: str
#GET 
class StudentResponse(BaseModel):
    id:int
    name:str
    age:int
    course: str
#PATCH
class StudentPatch(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    course:Optional[str]=None
class Config():  
    from_attributes=True  