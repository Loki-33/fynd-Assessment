from sqlalchemy import Null, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool
import os 
from dotenv import load_dotenv
load_dotenv()

DATABASE_URI = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URI, poolclass=NullPool)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
