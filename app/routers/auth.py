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
    existing_user=db.query(Users).filter(Users.username==user.username).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    existing_email=db.query(Users).filter(Users.email==user.email).first()

    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="email already registered"
        )

    hashed_password=hash_password(user.password)

    db_user=Users(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(db_user)

    db.commit()

    return db_user