from fastapi import APIRouter,Depends,status
from ..database import get_db
from .. import schemas,oauth2
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post("",response_model=schemas.ShowUser,status_code=status.HTTP_201_CREATED, tags=['Users'])
def create_user(request: schemas.User,db : Session = Depends(get_db)):
    return user.create_user(request,db)
    


@router.get("",response_model=list[schemas.ShowUser], tags=['Users'])
def show_users(db : Session = Depends(get_db)):
    return user.show_users(db)


@router.get("/{id}",response_model=schemas.ShowUser, tags=['Users'])
def show_user(id:int ,db:Session=Depends(get_db)):
    return user.show_user(id,db)

@router.put("/{id}",response_model=schemas.ShowUser,status_code=status.HTTP_202_ACCEPTED, tags=['Users'])
def edit_user(id: int,request: schemas.User , db : Session = Depends(get_db),current_user :schemas.User= Depends(oauth2.get_current_user)):
    return user.edit_user(id,request,db,current_user)


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT, tags=['Users'])
def delete_user(id:int,db : Session = Depends(get_db)):
    return user.delete_user(id,db)















    