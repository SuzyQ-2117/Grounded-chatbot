# Grounded-chatbot
A starter project that uses an LLM to scrape/assess the Fandom wiki pages for the game Grounded

Flow Summary
	1.	Frontend sends { "question": "What is a Black Ox Beetle?" } to POST /ask
	2.	FastAPI receives it in main.py, validates with AskRequest
	3.	main.py passes the question to:
	•	wiki.py → gets wiki summary
	•	openai_utils.py → sends context to GPT-4
	4.	GPT-4 generates a reply
	5.	Response is returned as { "answer": "..." }