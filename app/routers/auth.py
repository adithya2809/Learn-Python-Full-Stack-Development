from fastapi import APIRouter, HTTPException, Depends,status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Users
from app.schemas.user import UserCreate,UserResponse
from app.utils.security import hash_password

router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def register(user: UserCreate,db: Session=Depends(get_db)):
    pass
