import requests


def buscar_clima():
    url = (
        "https://api.open-meteo.com/v1/forecast?"
        "latitude=-15.78&longitude=-47.93&current_weather=true"
    )

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        temperatura = dados["current_weather"]["temperature"]

        return {
            "temperatura": temperatura
        }

    return None


def recomendacao_clima(temp):
    if temp >= 30:
        return "Treino leve recomendado e hidratação reforçada."

    if temp <= 15:
        return "Boa condição para treino intenso."

    return "Clima equilibrado para treino moderado."