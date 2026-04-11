from src.storage import load_data, save_data
from datetime import datetime


def add_registro(tipo, tempo):
    if tempo <= 0:
        return False

    data = load_data()
    data.append({
        "tipo": tipo,
        "tempo": tempo,
        "data": datetime.now().strftime("%Y-%m-%d")
    })
    save_data(data)
    return True


def resumo():
    data = load_data()

    treino = sum(i["tempo"] for i in data if i["tipo"] == "treino")
    jejum = sum(i["tempo"] for i in data if i["tipo"] == "jejum")
    dias = len(set(i["data"] for i in data))

    return treino, jejum, dias


def calcular_streak():
    data = load_data()
    datas = sorted(set(i["data"] for i in data), reverse=True)

    streak = 0
    hoje = datetime.now()

    for d in datas:
        diff = (hoje - datetime.strptime(d, "%Y-%m-%d")).days
        if diff == streak:
            streak += 1
        else:
            break

    return streak