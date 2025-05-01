# this is the bot's thinking brain

# function for generating a reply
# call openai.ChatCompletion.create() using GPT-4
# return the model's messafe content

from openai import OpenAI
import os
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_answer(question: str, wiki_context: str) -> str:
    # Fallback if the wiki_context is empty or contains junk data
    if not wiki_context.strip() or wiki_context.strip().lower() in [
        "no wiki data found.",
        "no readable wiki paragraph found."
    ]:
        return "Sorry, I couldn’t find any relevant wiki info for that."

    system_prompt = (
        "You are an expert on the game *Grounded*. Answer the user's questions "
        "based only on the wiki data provided. Keep your responses concise, ideally "
        "under 2-3 sentences unless more detail is explicitly requested."
    )

    user_message = f"Context:\n{wiki_context}\n\nQuestion:\n{question}"

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,
        max_tokens=200
    )

    return response.choices[0].message.content.strip()