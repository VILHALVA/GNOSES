from config import *

def polinomio():

    print("📉 Bem-vindo ao Avaliador de Polinômios!")
    sleep(2)
    grau = VALOR_FLOAT("🔢Digite o grau do polinômio:\n>>>")
    coeficientes = []
    for i in range(int(grau) + 1):
        coeficiente = VALOR_FLOAT(f"🔵Digite o coeficiente do termo de grau {int(grau) - i}:\n>>>")
        coeficientes.append(coeficiente)
    x = VALOR_FLOAT("🔍 Digite o valor de x para avaliar o polinômio:\n>>>")
    resultado = sum(coef * (x ** (int(grau) - i)) for i, coef in enumerate(coeficientes))
    PROCESSANDO()
    expressao_polinomial = " + ".join(f"{coef}x^{int(grau) - i}" for i, coef in enumerate(coeficientes))
    LINHA(f"⚡O polinômio é: {expressao_polinomial}\n⭐O resultado para x = {x} é: {resultado}")

    FIM()


