from celery import shared_task
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from . import settings


@shared_task
def chatboty_trainer():
    chatbot = ChatBot(**settings.CHATTERBOT)

    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train based on the english corpus
    trainer.train("chatterbot.corpus.english")

    # Train based on english greetings corpus
    trainer.train("chatterbot.corpus.english.greetings")

    # Train based on the english conversations corpus
    trainer.train("chatterbot.corpus.english.conversations")




