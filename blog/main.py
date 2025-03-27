from fastapi import FastAPI,Depends,status,HTTPException
from . import schemas,models
from .database import engine,get_db
from sqlalchemy.orm import Session
from.hashing import Hash
from .routers import blog,user,authentication
app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
models.Base.metadata.create_all(bind=engine)

# @app.post("/blog",status_code=status.HTTP_201_CREATED, tags=['Blogs'])
# def create(request: schemas.Blog,db : Session = Depends(get_db)):
#     new_blog = models.Blog(title = request.title,body = request.body,user_id = 1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get("/blog",response_model=list[schemas.ShowBlog], tags=['Blogs'])
# def show_blogs(db : Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
    
#     return blogs

# @app.get("/blog/{id}",response_model=schemas.ShowBlog, tags=['Blogs'])
# def show_blog(id:int ,db:Session=Depends(get_db)):

#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
#     return blog


# @app.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
# def edit_blog(id: int,request: schemas.Blog , db : Session = Depends(get_db)):
#     eblog = db.query(models.Blog).filter(models.Blog.id == id)
#     print("hello")
#     print(request)
#     if not eblog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
#     eblog.update(request.dict(exclude_unset=True))
#     db.commit()
#     return {'message':f"Blog with id {id} updated successfully",'data':eblog.first()}


# @app.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT, tags=['Blogs'])
# def delete_blog(id:int,db : Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
#     db.commit()
#     return {'message':f"Blog with id {id} deleted successfully"}




# @app.post("/user",response_model=schemas.ShowUser,status_code=status.HTTP_201_CREATED, tags=['Users'])
# def create_user(request: schemas.User,db : Session = Depends(get_db)):
    
#     print(request)
#     new_user = models.User(name = request.name,email = request.email,password = Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get("/user",response_model=list[schemas.ShowUser], tags=['Users'])
# def show_users(db : Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     return users

# @app.get("/user/{id}",response_model=schemas.ShowUser, tags=['Users'])
# def show_user(id:int ,db:Session=Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} not found")
#     return user

# @app.put("/user/{id}",response_model=schemas.ShowUser,status_code=status.HTTP_202_ACCEPTED, tags=['Users'])
# def edit_user(id: int,request: schemas.User , db : Session = Depends(get_db)):
#     euser = db.query(models.User).filter(models.User.id == id)
#     if not euser.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} not found")
#     euser.update(request.dict(exclude_unset=True))
#     db.commit()
#     return euser.first()

# @app.delete("/user/{id}",status_code=status.HTTP_204_NO_CONTENT, tags=['Users'])
# def delete_user(id:int,db : Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} not found")
#     db.commit()
#     return {'message':f"User with id {id} deleted successfully"}















    