from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from blog import models
from ..database import get_db
from .. import schemas
from .. import oauth2

def get_all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    blogs = db.query(models.Blog).filter(models.Blog.user_id == current_user.id).all()
    return blogs

def get_one(id:int,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    return blog


def create_blog(request: schemas.Blog,db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    print("inside create blog")
    print(current_user)
    print(type(current_user))
    print("inside create blog after current user")
    new_blog = models.Blog(title = request.title,body = request.body,user_id = current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def edit_blog(id:int,request: schemas.Blog,db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    eblog = db.query(models.Blog).filter(models.Blog.id == id)
    print("hello")
    print(request)
    if eblog.first().user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"you dont have access to others blog")
    if not eblog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    eblog.update({"title" : request.title,"body" : request.body,"user_id" : current_user.id})
    db.commit()
    return {'message':f"Blog with id {id} updated successfully",'data':eblog.first()}
def delete_blog(id:int,db : Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if blog.first().user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"you dont have access to others blog")
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {'message':f"Blog with id {id} deleted successfully"}

# 