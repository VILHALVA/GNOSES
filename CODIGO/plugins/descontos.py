from config import *

def descontos():
    print("😎Agora vamos calcular o seu desconto...")
    sleep(3)
    preço = VALOR_FLOAT("😎Digite o seu valor original(R$):\n>>>")
    desconto = VALOR_FLOAT("😎Digite o seu desconto(%):\n>>>")
    pagar = preço - (preço * desconto / 100)   
    PROCESSANDO()
    LINHA(f"⚡Preço de R${preço:.2f}!\n⚡Com um desconto de {desconto:.0f}%!\n⭐Valor a pagar é de R${pagar:.2f}!")        
    FIM()