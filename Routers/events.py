from fastapi import APIRouter, Depends, HTTPException, Request, status
from Database.database import get_session
from Events.models import EventModel, UpdateEventModel
from typing import List
from .authenticate import authenticate

event_router = APIRouter(tags=["Events"])



@event_router.post("/add")
async def add_event(new_event: EventModel, session=Depends(get_session),user:str=Depends(authenticate)):
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {"message":"Event was created successfully."}

@event_router.get("/{id}", response_model=EventModel)
async def get_event(id:int, session=Depends(get_session))->EventModel:
    event = session.get(EventModel, id)
    if event:
        return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Event does not exist.")

# Test route 'curl -X 'GET' 'http://127.0.0.1:8000/event/ -H 'accept: application/json'

@event_router.put("/update/{id}", response_model=EventModel)
async def update_event(id:int,new_data:UpdateEventModel,session=Depends(get_session),user:str=Depends(authenticate)) -> EventModel:
    event = session.get(EventModel, id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for k, v in event_data.items():
            setattr(event,k, v)
            
        session.add(event)
        session.commit()
        session.refresh(event)
        return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event does not exist")

@event_router.delete("/delete/{id}")
async def delete_event(id:int, session=Depends(get_session), user:str=Depends(authenticate))->dict:
    event = session.get(EventModel, id)
    if event:
        session.delete(event)
        session.commit()
        
        return {"message":"Event was deleted successfully"}
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event does not exist.")
    