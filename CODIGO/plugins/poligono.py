from config import *

def poligono():
    print("📐Bem-vindo ao Calculador de Área de Polígono!")
    sleep(2)
    num_lados = VALOR_FLOAT("🔢Digite o número de lados do polígono regular:\n>>>")
    comprimento_lado = VALOR_FLOAT("📏Digite o comprimento do lado do polígono:\n>>>")
    apotema = comprimento_lado / (2 * math.tan(math.pi / num_lados))
    area_poligono = (num_lados * comprimento_lado * apotema) / 2
    PROCESSANDO()
    LINHA(f"⚡Número de lados do polígono: {num_lados}\n⚡Comprimento do lado do polígono: {comprimento_lado}\n⭐Área do polígono: {area_poligono:.4f}")

    FIM()


