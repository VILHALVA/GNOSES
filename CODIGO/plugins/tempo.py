from config import *

def tempo():
    print("😎Bem-vindo ao Conversor de Tempo!")
    sleep(1)
    minutos = VALOR_INT("😎Digite a quantidade de minutos para converter em horas:\n>>>")
    if minutos < 0:
        print("😠Valor inválido. Por favor, insira um número positivo de minutos.")
    else:
        PROCESSANDO()
        horas = minutos // 60
        minutos_restantes = minutos % 60
        LINHA(f"\n⚡ Conversão de Tempo ⚡\n")
        print(f"{minutos} minutos correspondem a {horas} horas e {minutos_restantes} minutos.")
        
    FIM()
