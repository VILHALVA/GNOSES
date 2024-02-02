def calcular_mmc(a, b):
    m = a
    n = b
    while n:
        m, n = n, m % n
    return a * b // m

def mmc():
    from AAAA import VALOR_INT, PROCESSANDO, linha, FIM
    
    num1 = VALOR_INT("😎Digite o primeiro número:\n>>>")
    num2 = VALOR_INT("😎Digite o segundo número:\n>>>")

    resultado = calcular_mmc(num1, num2)

    PROCESSANDO()
    linha(f"⭐O MMC de {num1} e {num2} é: {resultado}")
    FIM()
