def algebra():
    from time import sleep
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM

    print("🧮Vamos realizar uma operação algébrica!")
    sleep(2)
    termo1 = VALOR_FLOAT("🔢Digite o primeiro termo:\n>>>")
    termo2 = VALOR_FLOAT("🔢Digite o segundo termo:\n>>>")
    operacao = input("🤖Escolha a operação desejada (+ para soma, - para subtração, * para multiplicação, / para divisão):\n>>> ")
    while operacao not in ('+', '-', '*', '/'):
        print("⚠️ Operação inválida. Por favor, escolha uma operação válida.")
        operacao = input("🤖 Escolha a operação desejada (+ para soma, - para subtração, * para multiplicação, / para divisão):\n>>> ")
    resultado = 0
    if operacao == '+':
        resultado = termo1 + termo2
    elif operacao == '-':
        resultado = termo1 - termo2
    elif operacao == '*':
        resultado = termo1 * termo2
    elif operacao == '/':
        if termo2 != 0:
            resultado = termo1 / termo2
        else:
            print("⚠️Erro: Não é possível realizar a divisão quando o denominador é zero!")
            return
    PROCESSANDO()
    linha(f"⚡ O primeiro termo é: {termo1}\n⚡ O segundo termo é: {termo2}\n⭐ O resultado da operação ({operacao}) é: {resultado}")

    FIM()


