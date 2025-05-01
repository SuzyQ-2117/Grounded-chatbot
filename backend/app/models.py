# request & response models using pydantic 

# define AskRequest(BaseModel) with a `question: str`
# optionally define AskResponse(BaseModel) with an `answer: str`

from pydantic import BaseModel

# this expects a JSON body consisting of a string called "question"
class AskRequest(BaseModel):
    question: str

# expects a JSON body with a string called "answer"
class AskResponse(BaseModel): 
    answser: str