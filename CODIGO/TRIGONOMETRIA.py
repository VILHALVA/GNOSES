def trigonometria():
    from time import sleep
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM
    import math

    print("📐Bem-vindo à Calculadora Trigonométrica!")
    sleep(2)
    angulo_graus = VALOR_FLOAT("🔢Digite o valor do ângulo em graus:\n>>>")
    angulo_radianos = math.radians(angulo_graus)
    seno = math.sin(angulo_radianos)
    cosseno = math.cos(angulo_radianos)
    if angulo_graus % 180 == 90:
        tangente = "indefinida"
    else:
        tangente = math.tan(angulo_radianos)
    PROCESSANDO()
    linha(f"⚡Ângulo em graus: {angulo_graus}\n⚡Ângulo em radianos: {angulo_radianos}\n⭐Seno: {seno:.4f}\n⭐Cosseno: {cosseno:.4f}\n⭐Tangente: {tangente}")

    FIM()

