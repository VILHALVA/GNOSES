from config import *

def radar():
    velocidade = VALOR_FLOAT("😎Qual é a velocidade do seu carro?\n>>>")
    limite = VALOR_FLOAT("😎Qual é o limite de velocidade?\n>>>")
    PROCESSANDO()
    if velocidade > limite:
        print(f"😡MULTADO! Você excedeu o limite permitido; Que é {limite:.2f}km/h!!!")
        sleep(2)
        valor = VALOR_FLOAT("😤Para saber quanto você deve pagar, digite o valor da multa(R$) por cada km acima do limite:\n>>>")
        multa = (velocidade-limite)*valor
        PROCESSANDO()             
        LINHA(f"⭐Com velocidade do carro: {velocidade:.0f}km/h;\n⭐Sendo o limite de {limite:.0f}km/h;\n⭐Valor da multa por km é: R${valor:.2f};\n⭐Valor a pagar é: R${multa:.2f}!!!")            
        sleep(2)
    else:
        print("😎PARABÉNS!!! Você não excedeu o limite de velocidade!!!")
        sleep(2)
        print("😎Desejo boa sorte!!!")       
        FIM()