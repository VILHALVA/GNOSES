def segundo_grau():
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM
    
    a = VALOR_FLOAT("😎Digite o coeficiente 'a' da equação do segundo grau (ax² + bx + c = 0):\n>>>")
    b = VALOR_FLOAT("😎Digite o coeficiente 'b' da equação do segundo grau (ax² + bx + c = 0):\n>>>")
    c = VALOR_FLOAT("😎Digite o coeficiente 'c' da equação do segundo grau (ax² + bx + c = 0):\n>>>")
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + (delta)**0.5) / (2*a)
        x2 = (-b - (delta)**0.5) / (2*a)
        PROCESSANDO()
        linha(f"⭐A equação possui duas soluções reais:\n⭐x1 = {x1:.2f} e x2 = {x2:.2f}")
    elif delta == 0:
        x = -b / (2*a)
        PROCESSANDO()
        linha(f"⭐A equação possui uma solução real:\n⭐x = {x:.2f}")
    else:
        PROCESSANDO()
        linha("⭐A equação não possui soluções reais.")
    FIM()

