from config import *

def potenciacao():
    base = VALOR_FLOAT("😎Digite a base (a) da potenciação (a^b):\n>>>")
    expoente = VALOR_FLOAT("😎Digite o expoente (b) da potenciação (a^b):\n>>>")
    resultado = base ** expoente
    PROCESSANDO()
    LINHA(f"⭐O resultado da potenciação ({base}^{expoente}) é: {resultado}")
    FIM()

