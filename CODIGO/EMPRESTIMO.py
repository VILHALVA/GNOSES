def emprestimo():
    from AAAA import VALOR_FLOAT, VALOR_INT, PROCESSANDO, linha, FIM
    
    casa = VALOR_FLOAT("😎Qual é o valor da casa(R$)?\n>>>")
    salário = VALOR_FLOAT("😎Qual é o valor do seu salário(R$)?\n>>>")
    anos = VALOR_INT("😎Quantos anos de financiamento?\n>>>")
    prestação = casa / (anos * 12)
    mínimo = salário * 30 / 100
    PROCESSANDO()
    if prestação <= mínimo:
        resultado = "👍APROVADO"
    else:
        resultado = "👎NEGADO"     
    linha(f"⭐Pagar uma casa de R${casa:.2f};\n⭐Com salário de R${salário:.2f};\n⭐Em {anos} anos;\n⭐Prestação será de R${prestação:.2f};\n⭐Valor mínimo R${mínimo:.2f};\n⭐EMPRÉSTIMO:{resultado}!")                
    FIM()