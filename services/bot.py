import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from heapq import nlargest
import string
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from utlls import pega_temp


def viezzi_init():
    bot = ChatBot('Bot')
    ChatBot(
        'Viezzi',
        logic_adapters=[
            'chatterbot.logic.BestMatch',
            'chatterbot.logic.TimeLogicAdapter']
    )

    trainer = ListTrainer(bot)

    trainer.train([
        'oi',
        'ola, Seja bem vindo, me chamo Bot Viezzi, voce gostaria de saber alguma informação sobre o clima? ',
        'obrigado',
        'fico feliz em ajudar, gostaria de mais alguma informação sobre o clima?',
    ])
    request = input('you: ')
    if request.lower() in ['sim', 'claro', 'gostaria', "clima"]:
        print('ok')
        request = input("informe a cidade que gostaria de saber o clima: ")
        temp = pega_temp(request)
        print(temp)
        print("Viezzi: gostaria de mais alguma informação sobre o clima?")


    elif request.lower() in ['nao', 'não', 'sair']:

        print('ok, tchau')

        break
    elif request.lower() in ['porra', 'caralho', 'puta']:

        print('Viezzi: não posso fornecer esse tipo de informação, mas você pode me fazer perguntas sobre o clima')
        print("Viezzi: gostaria de alguma informação sobre o clima?")

    else:
        response = bot.get_response(request)
        print('Viezzi: ', response)

viezzi_init()