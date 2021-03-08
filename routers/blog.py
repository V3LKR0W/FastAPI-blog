from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from sqlalchemy.orm.session import Session
from .. import schemas, database, models, oauth2
from ..repository import blog
from typing import List

router = APIRouter()

@router.get('/blog', response_model=List[schemas.ShowBlog],tags=['blogs'])
def all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)
    
    
@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def destroy(id:int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)
    
@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id:int, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)
        


@router.get('/blog/{id}', status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog, tags=['blogs'])
def show(id:int, response: Response, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)
