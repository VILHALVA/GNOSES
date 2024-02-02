def primeiro_grau():
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM
    
    a = VALOR_FLOAT("😎Digite o coeficiente 'a' da equação do primeiro grau (ax + b = 0):\n>>>")
    b = VALOR_FLOAT("😎Digite o coeficiente 'b' da equação do primeiro grau (ax + b = 0):\n>>>")
    if a == 0:
        if b == 0:
            PROCESSANDO()
            linha("⭐A equação é indeterminada, pois possui infinitas soluções.")
        else:
            PROCESSANDO()
            linha("⭐A equação é impossível, pois não possui solução.")
    else:
        x = -b / a
        PROCESSANDO()
        linha(f"⭐A solução da equação do primeiro grau ({a}x + {b} = 0) é x = {x}")
    FIM()

