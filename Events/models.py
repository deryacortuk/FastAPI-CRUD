from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List 

class EventModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str 
    tags : List[str] = Field(sa_column=Column(JSON))
    location: str 
    
    class Config:
        
        schema_extra = {
            "example":{
                "title":"What is your event?",
                "description":"Event Details",
                "tags":["write code","read book",],
                "location":"Where?"
            }
        }
        
class UpdateEventModel(SQLModel):
    title: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]
    
    class Config:
        schema_extra = {
            "example":{
                "title":"What is your event?",
                "description":"Event Details",
                "tags":["write code","read book",],
                "location":"Where?"
            }
        }
        