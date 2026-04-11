from src.tracker import add_registro, resumo, calcular_streak
from src.ui import titulo, sucesso, erro, info
from src.config import META_TREINO

def main():
    while True:
        titulo("🌸 Discipline CLI")

        print("1. Registrar treino")
        print("2. Registrar jejum")
        print("3. Ver resumo")
        print("4. Ver streak")
        print("5. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            try:
                tempo = int(input("Minutos: "))
                if add_registro("treino", tempo):
                    sucesso("Treino registrado")
                else:
                    erro("Valor inválido")
            except:
                erro("Entrada inválida")

        elif opcao == "2":
            try:
                tempo = int(input("Horas: "))
                if add_registro("jejum", tempo):
                    sucesso("Jejum registrado")
                else:
                    erro("Valor inválido")
            except:
                erro("Entrada inválida")

        elif opcao == "3":
            treino, jejum, dias = resumo()
            info(f"Treino: {treino} min")
            info(f"Jejum: {jejum} h")
            info(f"Dias ativos: {dias}")

            if treino >= META_TREINO:
                sucesso("Meta semanal atingida 🎯")

        elif opcao == "4":
            streak = calcular_streak()
            info(f"Streak atual: {streak} dias 🔥")

        elif opcao == "5":
            break

        else:
            erro("Opção inválida")

if __name__ == "__main__":
    main()