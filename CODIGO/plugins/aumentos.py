from config import *

def aumentos():
    print("😎Agora vamos calcular o seu aumento...")
    sleep(3)
    preço = VALOR_FLOAT("😎Digite o seu valor original(R$):\n>>>")
    aumento = VALOR_FLOAT("😎Digite o seu aumento(%):\n>>>")
    pagar = preço + (preço * aumento / 100)  
    PROCESSANDO()
    LINHA(f"⚡Preço de R${preço:.2f}!\n⚡Com um aumento de {aumento:.0f}%!\n⭐Valor a pagar é de R${pagar:.2f}!")       
    FIM()      