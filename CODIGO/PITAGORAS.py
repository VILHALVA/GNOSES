def pitagoras():
    from time import sleep
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM

    print("📐Vamos usar o Teorema de Pitágoras para calcular a hipotenusa de um triângulo retângulo!")
    sleep(2)
    cateto1 = VALOR_FLOAT("📏Digite o comprimento do primeiro cateto (lado adjacente ao ângulo reto):\n>>>")
    cateto2 = VALOR_FLOAT("📐Digite o comprimento do segundo cateto (lado oposto ao ângulo reto):\n>>>")
    hipotenusa = (cateto1**2 + cateto2**2)**0.5
    PROCESSANDO()
    linha(f"⚡ O comprimento do primeiro cateto é: {cateto1}\n⚡ O comprimento do segundo cateto é: {cateto2}\n⭐ O comprimento da hipotenusa é: {hipotenusa}")

    FIM()
