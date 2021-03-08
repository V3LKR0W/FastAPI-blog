from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from starlette.status import HTTP_404_NOT_FOUND
from .. import schemas, database, models, token
from ..hashing import Hash

router = APIRouter()

@router.post('/login', tags=['authentication'])
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Username does not exist')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail='Invalid password')
    
    access_token = token.create_access_token(data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}
    
    return user