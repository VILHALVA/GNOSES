from config import *

def tales():
    print("📏 Vamos usar o Teorema de Tales para calcular segmentos proporcionais em um triângulo!")
    sleep(2)
    ponto_divisao = VALOR_FLOAT("📍Digite o ponto de divisão no lado (entre 0 e 1):\n>>>")
    lado_a = VALOR_FLOAT("📏 Digite o comprimento do lado A do triângulo:\n>>>")
    lado_b = VALOR_FLOAT("📏 Digite o comprimento do lado B do triângulo:\n>>>")
    segmento_c = lado_a * ponto_divisao
    segmento_d = lado_b * ponto_divisao
    PROCESSANDO()
    LINHA(f"⚡O ponto de divisão no lado é: {ponto_divisao}\n⚡ O comprimento do lado A é: {lado_a}\n⚡ O comprimento do lado B é: {lado_b}\n⭐ O segmento C é: {segmento_c}\n⭐ O segmento D é: {segmento_d}")

    FIM()


