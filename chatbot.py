from flask import Flask, render_template, request # make sure you have flask to run 
from chatterbot import ChatBot  # pip install chatterbot
from chatterbot.trainers import ListTrainer  # method to train chatbot
from train import start_trainer

#import logging
#logging.basicConfig(level=logging.INFO)

#Running the Flask
app = Flask(__name__)

#Routing to our index.html file 
@app.route("/") 
def home():
    return render_template("index.html")

# initializing bad_chars_list
bad_chars = [";", ":", "!", "@", "#", "$", "%", "^", "&", "(", ")", "?",",", ".", "~", "`", "[", "]", "{", "}", "-", "_"] 

bot = ChatBot(
    'Trump Bot', read_only=True,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Speak proper English,I do not understand.',
            'maximum_similarity_threshold': 0.90
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation',
        }])

trainer = ListTrainer(bot,  show_training_progress=False)  # set the trainer


#def chatbot():
    #while True:
       # request = input("You: ").lower()
        #for i in bad_chars:
        #    request = request.replace(i, '')  # using replace() to remove bad_chars
       # request_que = request.split(" ")
        #response = bot.get_response(request)
      #  print("Trump: " + str(response))


#chatbot() # Enable this if you want to chat in console

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))# Get the response of the Trump chat bot.


if __name__ == "__main__": #Running the bot on the web
    app.run()