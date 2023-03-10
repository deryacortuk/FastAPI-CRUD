from fastapi import APIRouter, HTTPException, status,Depends
from Database.database import get_session
from Events.models import EventModel, UpdateEventModel
from typing import List
from Users.authenticate import HashPassword
from Users.models import UserModel
from fastapi.security import OAuth2PasswordRequestForm
from Users.token import verify_access_token, create_access_token
from Users.schemas import Account,TokenResponse
from sqlmodel import select

user_router = APIRouter(tags=["User"])

hass_password = HashPassword()

@user_router.post("/signup")
async def user_register(user:Account, session=Depends(get_session)):
    new_user = UserModel(username=user.username, password=hass_password.create_hash(user.password),email=user.email)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"Your account was created successfully"}

@user_router.post("/login", response_model=TokenResponse)
async def login_user(user:OAuth2PasswordRequestForm=Depends(), session = Depends(get_session)):
    statement = select(UserModel).where(UserModel.username==user.username)
    user_exist = session.exec(statement).first()
    
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User is not exist.")
    if hass_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.username)
        return {"access_token":access_token, "token_type":"Bearer"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid")

