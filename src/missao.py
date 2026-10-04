
def menu():
    print("Bem vindo! O programa a seguir verificará se um robô tem energia suficiente para realizar uma missão.")
    print("Por favor, insira os valores numéricos a seguir para prosseguir")

def solicitar_usuario():
    bateria_atual = input("Bateria atual (em porcentagem, de 0-100): ")
    duracao_missao = input("Duração da missão (minutos): ")
    consumo_por_minuto = input("Consumo por minuto (em pontos percentuais): ")
    return bateria_atual, duracao_missao, consumo_por_minuto

menu()
solicitar_usuario()
