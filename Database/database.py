from sqlmodel import SQLModel,Session, create_engine
from Events.models import EventModel

database_file = "events.db"
database_connection_string = f"sqlite:///./{database_file}"

engine_url = create_engine(database_connection_string, echo=True, connect_args={"check_same_thread":False})

def conn_db():
    SQLModel.metadata.create_all(engine_url)
    
def get_session():
    with Session(engine_url) as session:
        yield session
        
