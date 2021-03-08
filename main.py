from api.routers import authentication
from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm.session import Session
from starlette.status import HTTP_404_NOT_FOUND
from . import schemas, models
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from .hashing import Hash
from typing import List
from .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)






