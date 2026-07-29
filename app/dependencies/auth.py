from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session

from jose import jwt,JWTError

from app.database import get_db
from app.config import SECRET_KEY
from app.models import Users
from app.utils.jwt import ALGORITHM
oauth2_scheme=OAuth2PasswordBearer(
    tokenUrl="auth/login"
)

def get_current_user(
        token:str=Depends(oauth2_scheme),
        db:Session=Depends(get_db)
):
    try:
        payload=jwt.decode(token,
                       SECRET_KEY,
                       algorithms=[ALGORITHM]
                       )

        username=payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="could not validate credentials"
            )
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate credentials")

    db_user=db.query(Users).filter(Users.username==username).first()

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )

    return db_user