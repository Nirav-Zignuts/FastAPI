from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import models,token
from ..database import get_db
from ..hashing import Hash

router = APIRouter(
    tags=['authentication']
)

@router.post('/login')
def login(request :OAuth2PasswordRequestForm= Depends() ,db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    print(user)
    if not user:
        print("inside not user")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User Doesnt Exists')
    if not Hash.verify(request.password,user.password):
        print("inside not hash verify")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid Credentials")
    

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}
 