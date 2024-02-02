def potenciacao():
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM
    
    base = VALOR_FLOAT("😎Digite a base (a) da potenciação (a^b):\n>>>")
    expoente = VALOR_FLOAT("😎Digite o expoente (b) da potenciação (a^b):\n>>>")
    resultado = base ** expoente
    PROCESSANDO()
    linha(f"⭐O resultado da potenciação ({base}^{expoente}) é: {resultado}")
    FIM()

