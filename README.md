

## Description
You can ask it various questions on topics that you think Trump would know
money,richness,wealth,iran,china, his father, the election etc.

## Local Setup:
 1. Ensure that Python, Flask, SQLAlchemy, and ChatterBot are installed (either manually, or run `pip install -r requirements.txt`).
 2. Run *app.py* with `python app.py`.
 3. The demo will be live at [http://localhost:5000/](http://localhost:5000/)


## Install the required packages:
Type in cmd : pip install -r requirements.txt

## How to use:
- Once the chatbot is active
- You type in a question
- The trump chatbot will analyze the question and based on its trained data
- It will reply with the best matched answer.






I will also provide a video tutorial demo on my youtube channel:
https://www.youtube.com/channel/UCOUrASPLv0as6m6N5cgQQcA/featured?view_as=subscriber



Build Process
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


## Link
1.Github Link:

2.Youtube Demo:

## Recommended
- You will need to have pip and atleast Python version 3.7 64 bit to install python packages
- Ensure your python is installed correctly in PATH



