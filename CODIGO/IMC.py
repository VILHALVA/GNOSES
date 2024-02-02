def imc():
    from time import sleep
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM
    
    print('😎Agora irei calcular o seu IMC (Índice de massa corporal),para saber se você está em forma.')
    sleep(3)        
    altura = VALOR_FLOAT("😎Digite sua altura em metros:\n>>>")
    peso = VALOR_FLOAT("😎Digite o seu peso em Kg:\n>>>")         
    imc = peso / altura ** 2       
    PROCESSANDO()
    linha(f"⚡Seu Peso é: ({peso:.2f})!\n⚡Sua altura é: ({altura:.2f})!\n⭐Seu IMC é {imc:.2f}!")       
    if imc < 16:
        linha("⭐RESULTADO: Seu estado é magreza grave!")
    elif imc < 17:
        linha("⭐RESULTADO: Seu estado é magreza moderada!")
    elif imc < 18.5:
        linha("⭐RESULTADO: Seu estado é magreza leve!")
    elif imc < 25:
        linha("⭐RESULTADO: Você é Saudável!")
    elif imc < 30:
        linha("⭐RESULTADO: Sobrepeso!")
    elif imc < 35: 
        linha("⭐RESULTADO: Obesidade Grau I!")
    elif imc < 40:
        linha("⭐RESULTADO: Obesidade Grau II!")
    else:
        linha("⭐RESULTADO: Obesidade Grau III!")     
    FIM()