from config import *

def binomio():
    print("📊Bem-vindo ao Expansor de Binômios!")
    sleep(2)
    a = VALOR_FLOAT("🔵Digite o coeficiente do primeiro termo (a):\n>>>")
    b = VALOR_FLOAT("🔴Digite o coeficiente do segundo termo (b):\n>>>")
    n = VALOR_FLOAT("🔢Digite o expoente (n):\n>>>")
    resultado = []
    for k in range(int(n) + 1):
        coeficiente_binomial = comb(int(n), k)
        termo = f"{coeficiente_binomial} * ({a}^{int(n) - k}) * ({b}^{k})"
        resultado.append(termo)
    expressao_expandida = " + ".join(resultado)
    PROCESSANDO()
    LINHA(f"⚡A expansão de ({a} + {b})^{int(n)} é:\n{expressao_expandida}")

    FIM()


