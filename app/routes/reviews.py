from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session 
from database import SessionLocal 
from models import Review 
from schemas import ReviewSubmit, ReviewResponse
from llm import generate_ai_outputs

router = APIRouter(prefix='/reviews', tags=['reviews'])

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

@router.post('/submit', response_model=ReviewResponse)
def submit_review(payload: ReviewSubmit, db: Session=Depends(get_db)):
    review_text = payload.review.strip() 
    if not review_text:
        raise HTTPException(status_code=400, detail='Review cannot be empty')
    truncated = review_text[:2000]
    ai = generate_ai_outputs(review_text)
    review = Review(
        rating=payload.rating,
        user_review=truncated,
        ai_response=ai['ai_response'],
        ai_summary=ai['ai_summary'],
        ai_actions=ai['ai_actions']
    )
    try:
        db.add(review)
        db.commit()
        db.refresh(review)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail='Faild to save review')

    return {
        'status': 'success',
        'ai_response': ai['ai_response']
    }

@router.get('/list')
def submit_reviews(db: Session=Depends(get_db)):
    reviews = db.query(Review).order_by(Review.created_at.desc()).all() 

    return {
        'reviews': [
            {
                'rating': r.rating,
                'review': r.user_review,
                'ai_summary': r.ai_summary,
                'ai_actions': r.ai_actions,
                'created_at': r.created_at.isoformat()
            }
            for r in reviews 
        ]
    }
