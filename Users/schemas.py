from pydantic import BaseModel, EmailStr
from typing import List, Optional
from Events.models import EventModel

class Account(BaseModel):
    username: str 
    email: EmailStr  
    password: str  
   
    

    
class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    