# this is the bot's thinking brain

# function for generating a reply
# call openai.ChatCompletion.create() using GPT-4
# return the model's messafe content

from openai import OpenAI
import os
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_answer(question: str, wiki_context: str) -> str:
    system_prompt = (
        "You are a helpful assistant who uses wiki information to answer user questions "
        "about the game Grounded. Use the provided context to respond clearly and concisely."
    )

    user_message = f"Context:\n{wiki_context}\n\nQuestion:\n{question}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()