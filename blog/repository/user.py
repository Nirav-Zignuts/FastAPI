from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from ..database import get_db
from ..hashing import Hash
from .. import schemas
from .. import models


def create_user(request:schemas.User,db:Session=Depends(get_db)):
    print(request)
    new_user = models.User(name = request.name,email = request.email,password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show_users(db:Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

def show_user(id:int,db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} not found")
    return user


def edit_user(id:int ,request : schemas.User,db: Session = Depends(get_db)):
    euser = db.query(models.User).filter(models.User.id == id)
    if not euser.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} not found")
    euser.update(request.dict(exclude_unset=True))
    db.commit()
    return euser.first()


def delete_user(id:int , db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} not found")
    db.commit()
    return {'message':f"User with id {id} deleted successfully"}