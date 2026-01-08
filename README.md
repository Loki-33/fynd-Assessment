# AI FEEDBACK SYSTEM 

A full-stack application for collecting and analyzing customer review using llm model(NVIDIA: Nemotron 3 Nano 30B A3B)

## LIVE DEMO 
- **Frontend**: 
  - **User**: https://fynd-assessment-front.onrender.com/user 
  - **Admin**: https://fynd-assessment-front.onrender.com/admin        
- **API Documentation**: https://fynd-assessment-api.onrender.com/docs 

## FEATURES
- **Review Submission**: Users can submit ratings (1-5) and detailed feedback
- **AI-Powered Analysis**: 
  - Automated response generation for customer engagement
  - Intelligent review summarization
  - Actionable insights extraction
- **Admin Dashboard**: View all reviews with AI analysis
- **Error Handling**: Gracefully handles empty reviews, long text, and API failures

### BACKEND 
- **FastAPI**: High-performance Python web framework
- **SQLAlchemy**: ORM for database operations
- **PostgreSQL**: Primary database
- **OpenRouter**: LLM API for AI processing
- **Pydantic**: Data validation and serialization

### FRONTEND
- **Next.js**: React framework with server-side rendering
- **React**: Component-based UI

### DEPLOYMENT
- **Render**: Backend, frontend, and database hosting
- **Git**: Version control and CI/CD

## LOCAL RUNNING 

### BACKEND-SERVER 
1. cd app
2. Install the requirements using `pip install -r requirements.txt`
3. Set Environment Variables 
  - echo "DATABASE_URL=postgresql://localhost/yourdb" > .env
  - echo "OPENROUTER_API_KEY=your_key_here" >> .env
4. Run server: `uvicorn main:app --reload`

### FRONTEND-SERVER
1. cd Frontend
2. Set Environment Variables
  - echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
3. npm install 
4. npm run dev 


