import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from heapq import nlargest
import string
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from . import utils


def viezzi_init(request, esperando_clima):
    if not request:
        return
    
    bot = ChatBot('Bot')
    ChatBot(
        'Viezzi',
        logic_adapters=[
            'chatterbot.logic.BestMatch',
            'chatterbot.logic.TimeLogicAdapter']
    )

    trainer = ListTrainer(bot)
    utils.json_train_bot(trainer)

    print(esperando_clima)
    if request.lower() in ['sim', 'claro', 'gostaria', "clima"]:
        esperando_clima = True
        return "Informe a cidade que gostaria de saber o clima!!"
    elif esperando_clima:
        print('esperando clima')
        response = utils.pega_temp(request)
        esperando_clima = False
        return [response, "gostaria de mais alguma informação sobre o clima?"]
    elif request.lower() in ['nao', 'não', 'sair']:
        utils.export_json(bot)
        return "Ok, adeus"
    elif request.lower() in ['porra', 'caralho', 'puta']:
        respostas = [
            "não posso fornecer esse tipo de informação, mas você pode me fazer perguntas sobre o clima",
            "gostaria de alguma informação sobre o clima?",
        ]
        return respostas
    else:
        response = bot.get_response(request)

        return response
