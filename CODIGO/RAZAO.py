def razao():
    from time import sleep
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM

    print("🔢Bem-vindo à Calculadora de Razão!")
    sleep(2)
    valor1 = VALOR_FLOAT("🔢Digite o primeiro valor:\n>>>")
    valor2 = VALOR_FLOAT("🔢Digite o segundo valor:\n>>>")
    if valor2 == 0:
        linha("⚠️O segundo valor não pode ser zero. A razão é indefinida.")
    else:
        razao = valor1 / valor2
        PROCESSANDO()
        linha(f"⚡A razão entre {valor1} e {valor2} é: {razao:.4f}")

    FIM()

