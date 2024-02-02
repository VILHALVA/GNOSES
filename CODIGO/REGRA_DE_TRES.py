def regra_de_tres():
    from time import sleep
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM

    print("➗Bem-vindo à Calculadora de Regra de Três!")
    sleep(2)
    valor1 = VALOR_FLOAT("➗Digite o primeiro valor conhecido:\n>>>")
    unidade1 = input("📏Digite a unidade do primeiro valor:\n>>>")
    valor2 = VALOR_FLOAT("➗Digite o segundo valor conhecido:\n>>>")
    unidade2 = input("📏Digite a unidade do segundo valor:\n>>>")
    valor_desconhecido = VALOR_FLOAT("➗Digite o valor a ser encontrado:\n>>>")
    unidade_desconhecida = input("📏Digite a unidade do valor a ser encontrado:\n>>>")
    if valor1 == 0:
        linha("⚠️ O denominador não pode ser zero. Impossível calcular.")
    else:
        resultado = (valor2 * valor_desconhecido) / valor1
        PROCESSANDO()
        linha(f"⚡{valor1} {unidade1} está para {valor2} {unidade2} assim como {valor_desconhecido} {unidade_desconhecida} está para {resultado:.2f} {unidade_desconhecida}")

    FIM()


