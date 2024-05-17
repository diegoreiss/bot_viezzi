import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from heapq import nlargest
import string
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from services.api import pega_temp

bot = ChatBot('Bot')
chatbot = ChatBot(
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
def preprocess_text_pt(text):
    tokens = word_tokenize(text.lower(), language='portuguese')
    stop_words = set(stopwords.words('portuguese'))
    words = [word for word in tokens if word.isalnum() and word not in stop_words and word not in string.punctuation]
    return " ".join(words)

while True:
    request = input('you: ')
    if request.lower() == 'sim':
        print('ok')
        request = input("informe a cidade que gostaria de saber o clima: ")
        pega_temp(request)
        print("Viezzi: gostaria de mais alguma informação sobre o clima?")

    elif request.lower() in ['nao', 'não', 'sair ', 'Sair']:
        print('ok, tchau')
        break
    else:
        response = bot.get_response(request)
        print('Viezzi: ', response)