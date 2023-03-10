from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List 
from pydantic import validator, EmailStr

class UserModel(SQLModel, table=True):
    id: int = Field(primary_key=True)
    username:str=Field(index=True)
    password:str = Field(min_length=6)
    email:EmailStr
    

    
