from config import *

def viagem():
    distância = VALOR_FLOAT("😎Qual é a distância da sua viagem(km)?\n>>>")
    preço = VALOR_FLOAT("😎Qual é o preço por km?\n>>>")        
    pagar = distância * preço
    PROCESSANDO()                
    LINHA(f"⭐Com a distância de {distância:.0f}km;\n⭐Preço por km sendo R${preço:.2f};\n⭐Valor a pagar é R${pagar:.2f}!")      
    if pagar <= 200:
        LINHA("😎MUITO BOM!!!")
    else:
        LINHA("💸QUE ABSURDO!!!")          
    FIM()