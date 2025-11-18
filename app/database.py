from sqlmodel import SQLModel
from sqlmodel import SQLModel, create_engine,Session

DATABASE_URL = "sqlite:///./users.db"
# DATABASE_URL = "postgresql://fast_api_user:password@localhost:5432/fastapi_login"
engine = create_engine(DATABASE_URL, echo=True)

def create_tables_database():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SQLModel.metadata.create_all(engine)