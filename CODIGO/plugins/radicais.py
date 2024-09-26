from config import *

def radicais():
    print("√🧮Bem-vindo à Calculadora de Radicais!")
    sleep(2)
    radical1 = VALOR_FLOAT("🔢Digite o valor do primeiro radical:\n>>>")
    indice1 = VALOR_FLOAT("🔢Digite o índice do primeiro radical:\n>>>")
    radical2 = VALOR_FLOAT("🔢Digite o valor do segundo radical:\n>>>")
    indice2 = VALOR_FLOAT("🔢Digite o índice do segundo radical:\n>>>")
    operacao = STRING("🤖Escolha a operação desejada (+ para soma, - para subtração, * para multiplicação, / para divisão):\n>>> ")
    while operacao not in ('+', '-', '*', '/'):
        print("⚠️Operação inválida. Por favor, escolha uma operação válida.")
        operacao = input("🤖Escolha a operação desejada (+ para soma, - para subtração, * para multiplicação, / para divisão):\n>>> ")
    resultado = 0
    if operacao == '+':
        resultado = math.sqrt(radical1**indice1) + math.sqrt(radical2**indice2)
    elif operacao == '-':
        resultado = math.sqrt(radical1**indice1) - math.sqrt(radical2**indice2)
    elif operacao == '*':
        resultado = math.sqrt(radical1**indice1 * radical2**indice2)
    elif operacao == '/':
        if radical2 != 0 and indice2 != 0:
            resultado = math.sqrt(radical1**indice1) / math.sqrt(radical2**indice2)
        else:
            print("⚠️Erro: Não é possível realizar a divisão quando o radical ou o índice é zero!")
            return
    PROCESSANDO()
    LINHA(f"⚡Primeiro radical: √{radical1}^{indice1}\n⚡Segundo radical: √{radical2}^{indice2}\n⭐Resultado da operação ({operacao}): √{resultado:.4f}")

    FIM()

