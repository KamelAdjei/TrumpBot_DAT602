
## Description
Trump Bot is an interactive simulation of a twitter conversation with the President of the USA, Donald Trump.
You can ask him various questions on topics related to Money,Wealth, His family, Trade deals,Iran,China, World war 3 and anything else that you think Trump would know about.

## Module
DAT 602

## About
This project was inspired by Women Reclaiming AI.I designed the chatbot as an accurate representation of how Donald Trump would text in a Twitter conversation.I believe he would lead the conversation with random ,rude and obnoxious words and have an arrogant attitude towards the questions asked.

I used a python library called Chatterbot to generate the responses.ChatterBot uses a selection of machine learning algorithms to produce different types of responses to the user.It starts off with no knowledge of how to communicate.As ChatterBot receives more input the number of responses that it can reply and the accuracy of each response in relation to the input statement increase.

The program selects the closest matching response by searching for the closest matching known statement that matches the input, it then chooses a response from the selection of known responses to that statement.

I initially wanted to make a chatbot similar to the project "The Infinite Guide" which uses an LSTM Recurrent Neural Network to respond, but I chose to rather implement that into my final year project.

## Local Setup:
 1. Ensure that Python, Flask, SQLAlchemy, and ChatterBot are installed (either manually, or run `pip install -r requirements.txt`).
 2. Run *chatbot.py* with `python chatbot.py`.
 3. The demo will be live at [http://localhost:5000/](http://localhost:5000/)


## Install the required packages:
Type in cmd : pip install -r requirements.txt


## How to use:
- Once the chatbot is active
- You type in a question
- The trump chatbot will analyze the question and based on its trained data
- It will reply with the best matched answer.


## Build Process
- Train in chatbot in train.py on a corpus of words Donald Trump mostly uses (files).
- After the bot has finished training, dbsqlite files will be created.
- Using these files, go to chatbot.py and open terminal
- run "python chatbot.py", this will open a development server using Flask
- You can start chatting with the bot.

If you would like to train it yourself then delete the following:
- file.txt
- db.sqlite and all db files
- sentence_tokenizer



## How to Deploy

- It will be deployed using Flask which is a framework written in Python used to build web applications.
- Simply type in cmd in folder "python chatbot.py" and a development server will be live.


## Once it's running, you can ask questions like:
- Do you trust news networks?
- how much do you earn
- is America Racists?
- Are you a misogynist?
- Tell me a joke
- How would you describe your life?

## Link
1.Youtube Video Demo: https://www.youtube.com/watch?v=fam8RvTTMMs


## Recommended
- You will need to have pip and atleast Python version 3.7 64 bit to install python packages
- Ensure your python is installed correctly in PATH


## Note
(Files) folder contains all the corpus that the chatbot was trained on.

