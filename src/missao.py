
def menu():
    print("Bem vindo! O programa a seguir verificará se um robô tem energia suficiente para realizar uma missão.")
    print("Por favor, insira os valores numéricos a seguir para prosseguir")


def bateria_usuario():
    bateria_atual = input("Bateria atual (em porcentagem, de 0-100): ")
    bateria_atual = bateria_atual.replace("%","")
    bateria_atual = float(bateria_atual)
    print(bateria_atual)
    return bateria_atual

def duracao_usuario():
    duracao_missao = input("Duração da missão (minutos): ")
    duracao_missao = duracao_missao.lower().replace("minutos","").replace("min","").replace("m","")
    duracao_missao = float(duracao_missao)
    print(duracao_missao)
    return duracao_missao

def consumo_usuario():
    consumo_por_minuto = input("Consumo por minuto (em pontos percentuais): ")
    consumo_por_minuto = consumo_por_minuto.replace("%","").replace("/min","").replace("/m","")
    consumo_por_minuto = float(consumo_por_minuto)
    print(consumo_por_minuto)
    return consumo_por_minuto



menu()
bateria = bateria_usuario()
duracao = duracao_usuario()
consumo = consumo_usuario()


if bateria > 100 or bateria < 0 or duracao <= 0 or consumo <= 0:
    print("Valor(es) Inválido(s)")
else:
    consumo_total = consumo * duracao
    if bateria > consumo_total:
        bateria_restante = bateria - consumo_total
        print("A missão pode ser concluída!")
        print("O consumo total foi de: ", consumo_total, "%")
        print("A bateria restante será de: ", bateria_restante,"%")
    elif bateria == consumo_total:
        print("A missão pode ser concluída com 0% restante!")
        print("O consumo total foi de: ", consumo_total, "%")
    else:
        bateria_faltante = consumo_total - bateria
        print("A missão não pode ser concluída, serão necessários mais", bateria_faltante, "%")