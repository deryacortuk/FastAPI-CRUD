from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from Database.database import conn_db
import uvicorn
from Routers.events import event_router
from Routers.users import user_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(event_router, prefix="/event")
app.include_router(user_router, prefix="/user")

@app.on_event("startup")
def on_startup():
    conn_db()

@app.get("/")
def home():
    return RedirectResponse(url="/event/")

origins = ["*"]
app.add_middleware(
CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)

if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    