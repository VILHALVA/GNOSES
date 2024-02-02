def calcular_mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def mdc():
    from AAAA import VALOR_INT, PROCESSANDO, linha, FIM
    
    num1 = VALOR_INT("😎Digite o primeiro número:\n>>>")
    num2 = VALOR_INT("😎Digite o segundo número:\n>>>")
    resultado = calcular_mdc(num1, num2)
    PROCESSANDO()
    linha(f"⭐O MDC de {num1} e {num2} é: {resultado}")
    FIM()
