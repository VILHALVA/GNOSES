def triangulos():
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM
    
    r1 = VALOR_FLOAT("😎Digite o primeiro segmento:\n>>>")
    r2 = VALOR_FLOAT("😎Digite o segundo segmento:\n>>>")
    r3 = VALOR_FLOAT("😎Digite o terceiro segmento:\n>>>")
    PROCESSANDO()         
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
        if r1 == r2 == r3:
            triângulo = "👍SIM;\n⭐TIPO: EQUILÁTERO!"
        elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
            triângulo = "👍SIM;\n⭐TIPO: ISÓSCELES!"
        elif r1 != r2 != r3 != r1:
            triângulo = "👍SIM;\n⭐TIPO: ESCALENO!"
    else:
        triângulo = "👎NÃO!"
    linha(f"⭐SEGMENTOS: {r1}, {r2} e {r3}!\n⭐TRIÂNGULO?:{triângulo}")              
    FIM()