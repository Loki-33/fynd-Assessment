from fastapi import FastAPI 
from database import Base, engine 
from routes import reviews 
from fastapi.middleware.cors import CORSMiddleware

#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
app = FastAPI(title='FEEDBACK SYSTEM')

origins = [
    "http://localhost:3000", 
    "https://*.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(reviews.router)


