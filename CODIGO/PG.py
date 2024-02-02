def pg():
    from AAAA import VALOR_INT, PROCESSANDO, linha, FIM
    
    a1 = VALOR_INT("😎Digite o primeiro termo (a1):\n>>>")
    r = VALOR_INT("😎Digite a razão (r):\n>>>")
    q = VALOR_INT("😎Digite a razão da PG (q):\n>>>")
    termo = a1
    cont = 1
    total = 0
    mais = 10

    while mais != 0:
        PROCESSANDO()
        total = total + mais
        while cont <= total:
            print(f"⭐{termo}›", end="")
            termo *= q
            cont += 1
        print("\n⛔PAUSA!!!")
        mais = VALOR_INT("😎Quantos termos você quer mostrar a mais?\n😎Digite 0 caso queira parar:\n>>>")

    linha(f"⛔FINALIZADO COM TOTAL {total} TERMOS!")
    FIM()

