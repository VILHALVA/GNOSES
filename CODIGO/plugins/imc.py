from config import *

def imc():
    print('😎Agora irei calcular o seu IMC (Índice de massa corporal),para saber se você está em forma.')
    sleep(3)        
    altura = VALOR_FLOAT("😎Digite sua altura em metros:\n>>>")
    peso = VALOR_FLOAT("😎Digite o seu peso em Kg:\n>>>")         
    imc = peso / altura ** 2       
    PROCESSANDO()
    LINHA(f"⚡Seu Peso é: ({peso:.2f})!\n⚡Sua altura é: ({altura:.2f})!\n⭐Seu IMC é {imc:.2f}!")       
    if imc < 16:
        LINHA("⭐RESULTADO: Seu estado é magreza grave!")
    elif imc < 17:
        LINHA("⭐RESULTADO: Seu estado é magreza moderada!")
    elif imc < 18.5:
        LINHA("⭐RESULTADO: Seu estado é magreza leve!")
    elif imc < 25:
        LINHA("⭐RESULTADO: Você é Saudável!")
    elif imc < 30:
        LINHA("⭐RESULTADO: Sobrepeso!")
    elif imc < 35: 
        LINHA("⭐RESULTADO: Obesidade Grau I!")
    elif imc < 40:
        LINHA("⭐RESULTADO: Obesidade Grau II!")
    else:
        LINHA("⭐RESULTADO: Obesidade Grau III!")     
    FIM()