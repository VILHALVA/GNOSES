from config import *

def geometria_analitica():
    print("📈 Bem-vindo à Geometria Analítica!")
    sleep(2)
    x1 = VALOR_FLOAT("🔵Digite a coordenada x do primeiro ponto:\n>>>")
    y1 = VALOR_FLOAT("🔵Digite a coordenada y do primeiro ponto:\n>>>")
    x2 = VALOR_FLOAT("🔴Digite a coordenada x do segundo ponto:\n>>>")
    y2 = VALOR_FLOAT("🔴Digite a coordenada y do segundo ponto:\n>>>")
    distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    PROCESSANDO()
    LINHA(f"⚡Coordenadas do primeiro ponto: ({x1}, {y1})\n⚡Coordenadas do segundo ponto: ({x2}, {y2})\n⭐Distância entre os dois pontos: {distancia:.4f}")
    if x1 != x2:
        coeficiente_angular = (y2 - y1) / (x2 - x1)
        coeficiente_linear = y1 - coeficiente_angular * x1
        LINHA(f"🔍Equação da reta: y = {coeficiente_angular:.4f}x + {coeficiente_linear:.4f}")
    else:
        LINHA("⚠️Os pontos estão na mesma linha vertical. A equação da reta não pode ser determinada.")

    FIM()