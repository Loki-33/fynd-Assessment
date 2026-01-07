from sqlalchemy import Column, DateTime, Nullable, String, Integer 
from sqlalchemy.sql import func 
from .database import Base 
import uuid 

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    rating = Column(Integer, nullable=False)
    user_review = Column(String, nullable=False)
    ai_response = Column(String, nullable=True)
    ai_summary = Column(String, nullable=True)
    ai_actions = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


