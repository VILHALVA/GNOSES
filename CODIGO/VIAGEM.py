def viagem():
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM
    
    distância = VALOR_FLOAT("😎Qual é a distância da sua viagem(km)?\n>>>")
    preço = VALOR_FLOAT("😎Qual é o preço por km?\n>>>")        
    pagar = distância * preço
    PROCESSANDO()                
    linha(f"⭐Com a distância de {distância:.0f}km;\n⭐Preço por km sendo R${preço:.2f};\n⭐Valor a pagar é R${pagar:.2f}!")      
    if pagar <= 200:
        linha("😎MUITO BOM!!!")
    else:
        linha("💸QUE ABSURDO!!!")          
    FIM()