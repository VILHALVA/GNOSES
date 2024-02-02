def votacao():
    import datetime
    from AAAA import VALOR_INT, PROCESSANDO, FIM
    
    atual = datetime.date.today().year
    ano_nascimento = VALOR_INT("😎Digite o ano do seu nascimento:\n>>>")
    PROCESSANDO()
    idade = atual - ano_nascimento
    if idade >= 16 and idade < 18:
        print(f"⭐Você tem {idade} anos. Pode votar, mas o voto é opcional.")
    elif idade >= 18 and idade <= 60:
        print(f"⭐Você tem {idade} anos. Pode votar obrigatoriamente.")
    elif idade > 60:
        print(f"⭐Você tem {idade} anos. O voto é opcional.")
    else:
        print(f"⭐Você tem {idade} anos. Não pode votar.")
    FIM()

