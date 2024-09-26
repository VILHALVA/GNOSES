from config import *

def logaritmos():
    print("📊Bem-vindo à Calculadora de Logaritmos!")
    sleep(2)
    base = VALOR_FLOAT("🔢Digite a base do logaritmo:\n>>>")
    numero = VALOR_FLOAT("🔢Digite o número para o qual deseja calcular o logaritmo:\n>>>")
    resultado = math.log(numero, base)
    PROCESSANDO()
    LINHA(f"⚡Base do logaritmo: {base}\n⚡Número: {numero}\n⭐Resultado do logaritmo: {resultado:.4f}")

    FIM()


