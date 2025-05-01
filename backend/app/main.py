# this is the main entry point for starting the app

# create my fastapi app here including: 
# CORS middleware
# /ask endpoint

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import AskRequest, AskResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.post("/ask", response_model=AskResponse)
def ask_question(data: AskRequest):
    return AskResponse(answer=f"You asked: {data.question}")