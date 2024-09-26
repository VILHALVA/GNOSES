from config import *

def conjuntos():
    print("🔄Bem-vindo ao Cálculo de Domínio e Conjunto de Imagem!")
    sleep(2)
    conjunto_dominio = set(map(VALOR_INT, input("🔢Digite os elementos do domínio separados por espaços (ex: 1 2 3):\n>>>").split()))
    relacoes = []
    for elemento1 in conjunto_dominio:
        linha_relacao = set(map(VALOR_INT, input(f"🔄Digite as relações para o elemento {elemento1} separadas por espaços (ex: 1 2 3):\n>>>").split()))
        relacoes.extend([(elemento1, elemento2) for elemento2 in linha_relacao])
    domínio = set(elemento[0] for elemento in relacoes)
    conjunto_imagem = set(elemento[1] for elemento in relacoes)
    PROCESSANDO()
    LINHA(f"⚡Domínio da relação: {domínio}\n⚡Conjunto de Imagem da relação: {conjunto_imagem}")

    FIM()

