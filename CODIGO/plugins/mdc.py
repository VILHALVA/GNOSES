from config import *

def calcular_mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def mdc():
    num1 = VALOR_INT("😎Digite o primeiro número:\n>>>")
    num2 = VALOR_INT("😎Digite o segundo número:\n>>>")
    resultado = calcular_mdc(num1, num2)
    PROCESSANDO()
    LINHA(f"⭐O MDC de {num1} e {num2} é: {resultado}")
    FIM()
