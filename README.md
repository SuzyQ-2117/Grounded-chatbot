# Grounded-chatbot
A starter project that uses an LLM to scrape/assess the Fandom wiki pages for the game Grounded

## Flow Summary
1.	Frontend sends { "question": "What is a Black Ox Beetle?" } to GET `/ask?question=Black%20Ox%20Beetle` or similar
2.	FastAPI receives it in main.py, validates with AskRequest
3.	main.py passes the question to:
	* wiki.py → gets wiki summary
	* openai_utils.py → sends context to GPT-4
4.	GPT-4 generates a reply
5.	Response is returned as { "answer": "..." }

# Setting up the Backend

## 1. Installing Python 3.12

I'm developing on a MacBook so I've only included instructions for installing and configuring Python 3.12 in MacOS.

This guide assumes you have installed Homebrew. If you do not have Homebrew installed, [check the Homebrew website here](https://brew.sh/) for more info.

Open a new terminal window and run:
``` sh
brew install python@3.12
```

To make sure your shell uses Python 3.12 by default, you’ll need to update your shell profile (e.g., .zshrc, .bash_profile, etc.):
``` sh
echo 'export PATH="/opt/homebrew/opt/python@3.12/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Alternatively, you can download the Python 3.12 installer directly from the [official Python website](https://www.python.org/downloads/mac-osx/).

To verify your Python installation is complete, run: 
``` sh
python3 --version
```

You should see a response that looks something like this:
``` sh
Python 3.12.x
```

## 2. Creating a Virtual Environment

Once Python is installed, you can create a virtual environment by running:
``` sh
python3 -m venv <venv-name>
```

You'll need to activate this by running: 
``` sh
source <venv-name>/bin/activate
```

Once your virtual environment is activated, you should see `(venv)` at the beginning or your terminal line (or whatever you named your  environment if you're not using `venv` specifically). The .gitignore file will automatically exclude virtual environments that are called `venv`.

You can exit the virtual environment by running: 
``` sh 
deactivate
```

## 3. Installing the backend app requirements

The app requirements contain a series of Python packages that the app uses to run. Without these, you will not be able to run the app. 

Make sure your virtual environment is active (as above) before installing packages. Once your virtual environment is active, run: 
``` sh
pip install -r backend/requirements.txt
```

You'll see some terminal output churning through as pip installs the packages for you.

## 4. Create the .env file

Copy the `.env.example` file and update the values:
``` sh
cp backend/.env.example backend/.env
```

Fill in your OpenAI key: you'll need one from [OpenAI](https://platform.openai.com/).

## 5. Starting the backend app

Still inside your virtual environment, you just need to run: 
``` sh 
cd backend
uvicorn app.main:app --reload
```

This will update your working directory to the backend/ folder and run the app. You should see this output in your terminal: 
```sh
INFO:     Will watch for changes in these directories: ['<directory-address-for-the-backend-folder>']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [97169] using StatReload
INFO:     Started server process [97171]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Each time you save any changes to the app code, this command ensures that the backend app is automatically reloaded to implement your changes. Do not close the terminal window you used to run this command as this will terminate the app. 

The FastAPI package automatically generates documentation for you based on your endpoints. You can [check out the docs for this app here](localhost:8000/docs).

To safely exit the app, use `CTRL+C` in the terminal window to stop the app from running. 


Making a test push to see if the workflow runs properly - final test push hopefully