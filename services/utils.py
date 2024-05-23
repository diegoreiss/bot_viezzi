import json

import requests
from django.conf import settings

def me():
    print(settings.BASE_DIR)
    print(load_json())

def pega_temp(cidade):
    api_key = "ccbff3a178263fe7bd130a13f0e90b8d"

    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}"

    requisicao = requests.get(link)
    data = requisicao.json()

    if requisicao.status_code == 200:
        if "main" in data and "weather" in data:
            temperatura = data['main']['temp']
            humidade = data['main']['humidity']

            return f"\nCidade: {cidade}\nTemperatura: {temperatura-273:.2g}°C\nHumidade: {humidade}%.\n"
        else:
            return "Não foi possível obter informações sobre o clima."
    else:
        return "Erro ao consultar a API de previsão do tempo."

def load_json():
    with open (settings.BASE_DIR / 'treinamento.json', 'r', encoding = 'utf-8') as file:
        conversations = json.load(file)
    return conversations

def json_train_bot(trainer):
    conversations = load_json()
    trainer.train(conversations)

def export_json(bot, filename='aprendizado.json'):
    conversa = [{'text': msg.text} for msg in bot.storage.filter()]

    with open(filename, 'w') as json_file:
        json.dump(conversa, json_file, indent=4)

def safe_chat(response):
    p_proib = ['porra', 'caralho', 'puta']

    for word in p_proib:
        if word in response.lower():
            return False
        return True

def safe_chat_response(bot, text):
    response = chatbot_response(bot, text)

    if safe_chat(response):
        return response
    else:
        return('Viezzi: não posso fornecer esse tipo de informação, mas você pode me fazer perguntas sobre o clima')

def chatbot_response(bot, text):
    if text:
        response = bot.get_response(text)
        return response.text
    else:
        return "Viezzi: Não entendi, repita sua pergunta"