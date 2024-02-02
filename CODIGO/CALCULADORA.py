def calcular(operacao, num1, num2):   
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "😠Erro: Divisão por zero."

def calculadora():
    from time import sleep
    from AAAA import VALOR_FLOAT, STRING, PROCESSANDO, FIM
    
    print("😎Calculadora Simples no Terminal!")
    sleep(1)
    print("😎Operações disponíveis: +, -, *, /")   
    while True:
        operacao = STRING("😎Digite a operação (+, -, *, /) ou 's' para encerrar:\n>>>")
        if operacao == 's':
            break
        if operacao not in ('+', '-', '*', '/'):
            print("😠Operação inválida. Tente novamente.")
            continue
        try:
            num1 = VALOR_FLOAT("😎Digite o primeiro número:\n>>>")
            num2 = VALOR_FLOAT("😎Digite o segundo número:\n>>>")
        except ValueError:
            print("😠Entrada inválida. Certifique-se de inserir números válidos.")
            continue
        PROCESSANDO()
        print()
        resultado = calcular(operacao, num1, num2)
        print(f"⚡Resultado: {resultado}\n")
    FIM()


