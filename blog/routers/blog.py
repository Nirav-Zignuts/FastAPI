from fastapi import APIRouter,Depends,status
from ..database import get_db
from .. import schemas,oauth2,models
from ..repository import blog
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)



@router.get("",response_model=list[schemas.ShowBlog])
def show_blogs(db : Session = Depends(get_db),current_user :schemas.User= Depends(oauth2.get_current_user)):
    return blog.get_all(db,current_user)

@router.get("/{id}",response_model=schemas.ShowBlog)
def show_blog(id:int ,db:Session=Depends(get_db),current_user :schemas.User= Depends(oauth2.get_current_user)):
    return blog.get_one(id,db)

@router.post("",response_model=schemas.ShowBlog,status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog,db : Session = Depends(get_db),current_user :schemas.User= Depends(oauth2.get_current_user)):
    return blog.create_blog(request,db,current_user)


@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def edit_blog(id: int,request: schemas.Blog , db : Session = Depends(get_db),current_user :schemas.User= Depends(oauth2.get_current_user)):
    return blog.edit_blog(id,request,db,current_user)


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int,db : Session = Depends(get_db),current_user :schemas.User= Depends(oauth2.get_current_user)):
    return blog.delete_blog(id,db,current_user)