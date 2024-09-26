from config import *

def tabuada():
    operacoes = {
        1: "Adição (+)",
        2: "Subtração (-)",
        3: "Multiplicação (*)",
        4: "Divisão (/)"
    }

    print("😎Bem-vindo ao programa de Tabuada!")
    for chave, operacao in operacoes.items():
        print(f"👉 [{chave}] {operacao}")

    escolha_operacao = VALOR_INT("😎Escolha o número da operação desejada:\n>>>")
    while escolha_operacao not in operacoes.keys():
        print("😠Opção inválida. Tente novamente!")
        escolha_operacao = VALOR_INT("😎Escolha o número da operação desejada:\n>>>")

    numero_tabuada = VALOR_INT("😎Digite um número para a tabuada (de 0 a 10):\n>>>")
    while not 0 <= numero_tabuada <= 10:
        print("😠Número fora da faixa permitida. Tente novamente!")
        numero_tabuada = VALOR_INT("😎Digite um número para a tabuada (de 0 a 10):\n>>>")

    PROCESSANDO()

    LINHA(f"\n⚡ Tabuada de {numero_tabuada} - {operacoes[escolha_operacao]} ⚡\n")

    for i in range(0, 11):
        if escolha_operacao == 1:
            resultado = numero_tabuada + i
        elif escolha_operacao == 2:
            resultado = numero_tabuada - i
        elif escolha_operacao == 3:
            resultado = numero_tabuada * i
        elif escolha_operacao == 4:
            if i != 0:
                resultado = numero_tabuada / i
            else:
                resultado = "Indefinido"

        print(f"{numero_tabuada} {'+' if escolha_operacao == 1 else '-' if escolha_operacao == 2 else '*' if escolha_operacao == 3 else '/'} {i} = {resultado}")

    FIM()

