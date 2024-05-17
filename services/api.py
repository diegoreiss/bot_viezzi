import requests


def pega_temp(cidade):
    api_key = "ccbff3a178263fe7bd130a13f0e90b8d"

    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}"

    requisicao = requests.get(link)
    data = requisicao.json()

    if requisicao.status_code == 200:
        if "main" in data and "weather" in data:
            temperatura = data['main']['temp']
            humidade = data['main']['humidity']
            ret =  f"\nCidade: {cidade}\nTemperatura: {temperatura}°C\nHumidade: {humidade}%.\n"
            print(ret)
        else:
            return "Não foi possível obter informações sobre o clima."
    else:
        return "Erro ao consultar a API de previsão do tempo."


