from config import *

def pa():
    n = VALOR_INT("😎Digite o valor:\n>>>")
    r = VALOR_INT("😎Digite a razão:\n>>>")
    termo = n
    cont = 1
    total = 0
    mais = 10
    while mais != 0:
        PROCESSANDO()
        total = total + mais
        while cont <= total:
            print(f"⭐{termo}›", end= "")    
            termo += r
            cont += 1
        print("\n⛔PAUSA!!!")
        mais = VALOR_INT("😎Quantos termos você quer mostrar a mais?\n😎Digite 0 caso queira parar:\n>>>")
    LINHA(f"⛔FINALIZADO COM TOTAL {total} TERMOS!")         
    FIM()