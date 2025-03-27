from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from blog import models
from ..database import get_db
from .. import schemas

def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

def get_one(id:int,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    return blog


def create_blog(request: schemas.Blog,db: Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title,body = request.body,user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def edit_blog(id:int,request: schemas.Blog,db:Session = Depends(get_db)):
    eblog = db.query(models.Blog).filter(models.Blog.id == id)
    print("hello")
    print(request)
    if not eblog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    eblog.update(request.dict(exclude_unset=True))
    db.commit()
    return {'message':f"Blog with id {id} updated successfully",'data':eblog.first()}
def delete_blog(id:int,db : Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    db.commit()
    return {'message':f"Blog with id {id} deleted successfully"}