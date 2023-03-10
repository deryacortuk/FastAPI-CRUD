from datetime import datetime
from jose import JWTError, jwt
import time
from fastapi import HTTPException, status

SECRET_KEY = "HS2349AYNT87NDJZXC9167"

def create_access_token(user:str)->str:
    payload = {
        "user":user, "expires":time.time() + 3600
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


def verify_access_token(token:str):    
    try:        
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        expire = data.get("expires")
        if expire is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="No access token supplied")
        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token expired!")
        return data
    except JWTError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid token")