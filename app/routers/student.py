from typing import Optional
from fastapi import HTTPException
from fastapi import APIRouter
from app.schemas.students import StudentResponse
from app.schemas.students import StudentUpdate
from app.schemas.students import StudentCreate
from app.schemas.students import StudentPatch
from fastapi import status

from sqlalchemy.orm import Session #Session is the object through which SQLAlchemy communicates with PostgreSQL.
from fastapi import Depends #tells fastapi:"Before running this endpoint, give me whatever get_db() returns."
from app.database import get_db #This prevents connection leaks.
from app.models import Student
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
@router.post("/students",response_model=StudentResponse,status_code=status.HTTP_201_CREATED)
def create_student(student:StudentCreate,db:Session=Depends(get_db)):  #THIS MEANS: FastAPI, please call get_db() and pass the resulting Session object into the db parameter.
    
    
    db_student = Student(
        name=student.name,
        age=student.age,
        course=student.course
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student
    
    

@router.get("/students/{id}",response_model=StudentResponse)
def get_student(id: int,db:Session=Depends(get_db)):

    student=db.query(Student).filter(Student.id==id).first()
    if student is None:
        raise HTTPException(status_code=404,detail="Student Not Found")
    else:
        return student
    
    
@router.get("/students",response_model=list[StudentResponse])
def get_students(db:Session=Depends(get_db)):
    students=db.query(Student).all()
    return students

@router.put("/students/{id}",response_model=StudentResponse)
def update_student(id:int,student_update:StudentUpdate,db: Session=Depends(get_db)):
    student=db.query(Student).filter(Student.id==id).first()
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
    )  
    
    student.name=student_update.name
    student.age=student_update.age
    student.course=student_update.course

    db.commit()
    db.refresh(student)

    return student
@router.patch("/students/{id}",response_model=StudentResponse)
def patch_student_update(id:int,patch_student:StudentPatch,db: Session=Depends(get_db)):
    student=db.query(Student).filter(Student.id==id).first()
    if student is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        datail="Student Not Found"
    )  
    update_data=patch_student.model_dump(exclude_unset=True)
    for key,pair in update_data.items():
        setattr(student,key,pair)

    db.commit()
    db.refresh(student)
    return student

@router.delete("/students/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id:int,db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.id==id).first()
    if student is None:    
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student Not Found"
        )
    db.delete(student)
    db.commit()
    
    return{
                "message":"student deleted successfully"
            }
    