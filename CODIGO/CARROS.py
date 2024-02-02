def carros():
    from time import sleep
    from AAAA import VALOR_FLOAT, VALOR_INT, PROCESSANDO, linha, FIM
    
    print("😎Irei Calcular para você o valor do aluguel de um carro!")
    sleep(3)
    valor_dia = VALOR_FLOAT("😎Me diga, quanto custa o aluguel por dia(R$)?\n>>>")
    valor_km = VALOR_FLOAT("😎Me responda, quanto custa um quilômetro rodado(R$)?\n>>>")
    dias = VALOR_INT("😎Por quantos dias foi alugado?\n>>>")
    km = VALOR_FLOAT("😎Quantos km você andou?\n>>>")
    pagar = (dias * valor_dia) + (km * valor_km)
    PROCESSANDO()         
    linha(f"  💰Considerando quê:\n⚡O valor por dia é R${valor_dia:.2f}!\n⚡O valor por km é R${valor_km:.2f}!\n⚡Você usou por {dias} dias!\n⚡Andou com o carro: {km:.2f}km!\n⭐O total a pagar é R${pagar:.2f}!")        
    FIM()