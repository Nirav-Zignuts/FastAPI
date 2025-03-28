
from fastapi import HTTPException,Depends,status
from fastapi.security import OAuth2PasswordBearer
from . import token
import jwt
from sqlalchemy.orm import Session
from . import schemas,models
from .database import get_db
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user(data:str= Depends(oauth2_scheme),db:Session = Depends(get_db)):
    print(data)
    email = None
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(data, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
        print(token_data)
        print("hello")
        print(f'{token_data.email} hello with token data')
        print("hello after token data")
        user = db.query(models.User).filter(models.User.email == token_data.email).first()
        print(user)
        print(user.email)
        if user is None:
            raise credentials_exception
        else:
            return user
        
    except jwt.PyJWTError:

        raise credentials_exception
            
    
    



    # return token.verify_token(data,credentials_exception)



    # 