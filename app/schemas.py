from pydantic import BaseModel, Field 
from typing import List 

class ReviewSubmit(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    review: str = Field(..., min_length=1)

class ReviewResponse(BaseModel):
    status: str 
    ai_response: str|None = None 
    message: str | None = None 

class ReviewAdmin(BaseModel):
    rating: int 
    review: str 
    ai_summary: str 
    ai_actions: str 
    created_at: str 


