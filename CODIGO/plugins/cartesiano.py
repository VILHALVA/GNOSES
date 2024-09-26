from config import *

def cartesiano():
    print("📊 Bem-vindo ao Plano Cartesiano!")
    sleep(2)
    x1 = VALOR_FLOAT("🔵Digite a coordenada x do primeiro ponto:\n>>>")
    y1 = VALOR_FLOAT("🔵Digite a coordenada y do primeiro ponto:\n>>>")
    x2 = VALOR_FLOAT("🔴 Digite a coordenada x do segundo ponto:\n>>>")
    y2 = VALOR_FLOAT("🔴 Digite a coordenada y do segundo ponto:\n>>>")
    distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    PROCESSANDO()
    LINHA(f"⚡ As coordenadas do primeiro ponto são: ({x1}, {y1})\n⚡ As coordenadas do segundo ponto são: ({x2}, {y2})\n⭐ A distância entre os dois pontos é: {distancia:.2f}")
    quadrante1 = "primeiro" if x1 > 0 and y1 > 0 else ""
    quadrante2 = "segundo" if x2 < 0 and y2 > 0 else ""
    quadrante3 = "terceiro" if x2 < 0 and y2 < 0 else ""
    quadrante4 = "quarto" if x1 > 0 and y1 < 0 else ""
    quadrantes = [quadrante1, quadrante2, quadrante3, quadrante4]
    quadrantes = [q for q in quadrantes if q]  
    if quadrantes:
        LINHA(f"🔍 Os pontos estão no {', '.join(quadrantes)} quadrante(s).")
    else:
        LINHA("🔍 Os pontos estão sobre os eixos ou no ponto de origem.")

    FIM()

