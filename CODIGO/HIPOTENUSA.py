def hipotenusa():
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM
    
    CO = VALOR_FLOAT("😎Digite o comprimento do cateto oposto(ex:34):\n>>>")
    CA = VALOR_FLOAT("😎Digite o complemento do cateto adjacente(ex:30):\n>>>")
    HP = (CO**2 + CA**2) ** (1/2)
    PROCESSANDO()         
    linha(f"  🈯Considerando quê:\n⚡O comprimento do CO é: {CO:.2f}!\n⚡O comprimento do CA é: {CA:.2f}!\n⭐A hipotenusa mede: {HP:.2f}!")                       
    FIM()