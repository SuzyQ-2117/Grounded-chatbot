# this is the main entry point for starting the app

# create my fastapi app here including: 
# CORS middleware
# /ask endpoint

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Query

from app.models import AskRequest, AskResponse
from app.wiki import get_page_extract

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/ask", response_model=AskResponse)
def ask_question(question: str = Query(..., description="The wiki page title to search")):
    context = get_page_extract(question.title())
    return AskResponse(answer=f"Wiki says: {context}")