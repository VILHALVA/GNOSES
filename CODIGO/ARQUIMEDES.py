def arquimedes():
    from time import sleep
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM
    import math

    print("📏Bem-vindo à Calculadora de Arquimedes!")
    sleep(2)
    raio = VALOR_FLOAT("🔵Digite o raio do círculo:\n>>>")
    perimetro = 2 * math.pi * raio
    area = math.pi * raio**2
    PROCESSANDO()
    linha(f"⚡O raio do círculo é: {raio}\n⭐Perímetro do círculo: {perimetro:.4f}\n⭐Área do círculo: {area:.4f}")

    FIM()
