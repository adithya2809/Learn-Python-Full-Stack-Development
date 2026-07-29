from fastapi import APIRouter, HTTPException, Depends,status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Users
from app.schemas.user import UserCreate,UserResponse
from app.utils.security import hash_password

from app.schemas.user import UserLogin
from app.utils.jwt import create_access_token
from app.utils.security import verify_password

from app.dependencies.auth import get_current_user

from fastapi.security import OAuth2PasswordRequestForm

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

@router.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    db_user=db.query(Users).filter(Users.username==form_data.username).first()
    print("User found:", db_user.username if db_user else None)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    if not verify_password(form_data.password,db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token=create_access_token(
        data={"sub":db_user.username}
        
    )

    return {
        "access_token":access_token,
        "token_type":"bearer"
    }

@router.get("/me")
def get_me(current_user:Users=Depends(get_current_user)):
    return current_user
