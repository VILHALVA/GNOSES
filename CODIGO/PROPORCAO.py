def proporcao():
    from time import sleep
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM

    print("🔄 Vamos calcular a proporção entre dois valores...")
    sleep(3)
    valor1 = VALOR_FLOAT("🔄Digite o primeiro valor:\n>>>")
    valor2 = VALOR_FLOAT("🔄Digite o segundo valor:\n>>>")
    if valor2 != 0:
        proporcao = valor1 / valor2
        PROCESSANDO()
        linha(f"⚡ O primeiro valor é: ({valor1:.2f})\n⚡ O segundo valor é: ({valor2:.2f})\n⭐ A proporção é: ({proporcao:.2f})")
    else:
        linha("⚠️Erro: Não é possível calcular a proporção quando o segundo valor é zero!")

    FIM()


