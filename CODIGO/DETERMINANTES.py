def determinantes():
    from time import sleep
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM
    import numpy as np

    print("📊Bem-vindo à Calculadora de Determinantes!")
    sleep(2)
    ordem = VALOR_FLOAT("🔢Digite a ordem da matriz (n x n):\n>>>")
    matriz = []
    for i in range(int(ordem)):
        linha_matriz = [VALOR_FLOAT(f"🔄Digite o elemento [{i + 1}][{j + 1}]: \n>>>") for j in range(int(ordem))]
        matriz.append(linha_matriz)
    determinante = np.linalg.det(matriz)
    PROCESSANDO()
    linha(f"⚡Matriz informada:\n{np.array(matriz)}\n⭐Determinante: {determinante:.4f}")

    FIM()
