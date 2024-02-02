def geometria_plana():
    from time import sleep
    from AAAA import VALOR_FLOAT, STRING, PROCESSANDO, linha, FIM
    
    print("📐Bem-vindo à Calculadora de Geometria Plana!")
    sleep(2)
    figura = STRING("🔺Escolha a figura geométrica (triângulo, quadrado, retângulo):\n>>> ").lower()
    if figura == "triângulo":
        base = VALOR_FLOAT("📏Digite a medida da base do triângulo:\n>>>")
        altura = VALOR_FLOAT("📏Digite a medida da altura do triângulo:\n>>>")
        area_triangulo = (base * altura) / 2
        PROCESSANDO()
        linha(f"⚡Base do triângulo: {base}\n⚡Altura do triângulo: {altura}\n⭐ Área do triângulo: {area_triangulo:.4f}")
    elif figura == "quadrado":
        lado_quadrado = VALOR_FLOAT("📏Digite a medida do lado do quadrado:\n>>>")
        area_quadrado = lado_quadrado**2
        PROCESSANDO()
        linha(f"⚡Lado do quadrado: {lado_quadrado}\n⭐Área do quadrado: {area_quadrado:.4f}")
    elif figura == "retângulo":
        base_retangulo = VALOR_FLOAT("📏Digite a medida da base do retângulo:\n>>>")
        altura_retangulo = VALOR_FLOAT("📏Digite a medida da altura do retângulo:\n>>>")
        area_retangulo = base_retangulo * altura_retangulo
        PROCESSANDO()
        linha(f"⚡Base do retângulo: {base_retangulo}\n⚡Altura do retângulo: {altura_retangulo}\n⭐Área do retângulo: {area_retangulo:.4f}")
    else:
        print("⚠️Figura geométrica inválida. Por favor, escolha entre triângulo, quadrado ou retângulo.")
        return

    FIM()


