from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from sqlalchemy.orm.session import Session
from .. import schemas, database, models
from ..hashing import Hash
from typing import List
from ..repository import users
from starlette.status import HTTP_404_NOT_FOUND

router = APIRouter()

@router.post('/user', response_model=schemas.ShowUser, tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return users.create_user(db,request)

@router.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
def get_user(id:int, db: Session = Depends(database.get_db)):
    return users.show(id,db)