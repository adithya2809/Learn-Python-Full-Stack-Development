from typing import Optional
from fastapi import HTTPException
from fastapi import APIRouter
from app.schemas.students import StudentResponse
from app.schemas.students import StudentUpdate
from app.schemas.students import StudentCreate
from fastapi import status

from sqlalchemy.orm import Session #Session is the object through which SQLAlchemy communicates with PostgreSQL.
from fastapi import Depends #tells fastapi:"Before running this endpoint, give me whatever get_db() returns."
from app.database import get_db #This prevents connection leaks.
router = APIRouter()

students_db=[]

@router.get("/")
def home():
    return {
        "message":"Welcome Again"
    }

@router.get("/users")
def get_users():
    return[
        {"id": 1, "name": "Aditya"},
        {"id": 2, "name": "Rahul"},
        {"id": 3, "name": "Priya"}
    ]

@router.get("/about")
def about():
    return {"project": "Python Full Stack API", "version": "1.0"}

@router.get("/users/{id}")
def get_userid(id:int):
    return {"user_id": id}

@router.get("/products")
def get_products(category :str, brand :Optional[str]=None):
    return{
        "category":category,
        "brand": brand
           }
next_id=1    
@router.post("/students")
def create_student(student:StudentCreate,db:Session=get_db):  #THIS MEANS: FastAPI, please call get_db() and pass the resulting Session object into the db parameter.
    global next_id
    
    
    student_data = {
        "id":next_id,
        "name":student.name,
        "branch":student.branch,
        "age":student.age
        }
    students_db.append(student_data)
    next_id+=1
    return student_data
    
    status_code=status.HTTP_201_CREATED
    

@router.get("/students/{id}",response_model=StudentResponse)
def get_student(id: int):

    for student in students_db:

        if student["id"] == id:
            return student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )
@router.get("/students")
def get_students():
    return students_db

@router.put("/students/{id}")
def update_student(id:int,student:StudentUpdate):

    for existing_student in students_db:
        if existing_student["id"]==id:
            existing_student["name"]=student.name
            existing_student["age"]=student.age
            existing_student["branch"]=student.branch
            existing_student["stats"]=student.stats

            return existing_student
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )    

@router.patch("/students/{id}")
def patch_student(id:int,student:StudentUpdate):
    for existing_student in students_db:
        if student.name is not None:
            existing_student["name"]=student.name
        if student.age is not None:
            existing_student["age"]=student.age
        if student.branch is not None:
            existing_student["branch"]=student.branch
        if student.stats is not None:    
            existing_student["stats"]=student.stats
        return students_db 
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        datail="Student Not Found"
    )       

@router.delete("students/{id}")
def delete_student(id:int):
    for student in students_db:
        if student["id"]==id:
            students_db.remove(student)
            return{
                "message":"student deleted successfully"
            }
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student Not Found"
        )