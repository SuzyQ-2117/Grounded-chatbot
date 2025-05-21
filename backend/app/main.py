# this is the main entry point for starting the app

# create my fastapi app here including: 
# CORS middleware
# /ask endpoint

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Query

from app.models import AskRequest, AskResponse
from app.wiki import get_page_extract
from app.openai_utils import generate_answer

from fastapi import FastAPI

app = FastAPI(
    title="Grounded Chatbot API",
    description="A FastAPI-powered service that answers questions about the game *Grounded* using context pulled from the Fandom wiki.",
    version="0.1.0",
    contact={
        "name": "Suzy",
        "url": "https://github.com/SuzyQ-2117/grounded-chatbot"
    }
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/ask", response_model=AskResponse)
def ask_question(question: str = Query(...)):
    context = get_page_extract(question.title())
    gpt_response = generate_answer(question, context)
    return AskResponse(answer=gpt_response)