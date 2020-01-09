from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ListTrainer #method to train chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

#Training the bot
def start_trainer():
    bot = ChatBot(
    'Trump', read_only=True,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I do not understand.',
            'maximum_similarity_threshold': 0.90
        }])
    trainer = ListTrainer(bot) #set the trainer
    for _file in os.listdir('files'):
        chats = open('files/' + _file, 'r',encoding='latin-1').readlines()
        trainer.train(chats)

try:
    file=open("file.txt", 'r')#If this file is present then you dont need to train the bot
except FileNotFoundError:
    start_trainer()
    file=open("file.txt",'w')#If this file is not present then you need to train the bot
