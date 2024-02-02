def entrevista():
    from time import sleep
    from AAAA import VALOR_INT, STRING, PROCESSANDO, linha, FIM

    print("🔺AVISO: Essa entrevista se trata apenas de uma SIMULAÇÃO!!!")
    sleep(3)
    print("😎Seja bem vindo a mais uma entrevista de emprego genérica.")
    sleep(3)   
    nome = STRING("😎Qual é o seu nome?\n>>>").upper()
    if "SAMUEL" in nome or "DANIEL" in nome or "LUCAS" in nome or "MARIA" in nome or "ANA" in nome:
        print("😍Que nome lindo você tem!")
    else: 
        print("😒Seu nome é tão comum!")
    sleep(3)       
    sexo = STRING("😎Informe o seu sexo[M/F]:\n>>>").upper()[0]
    while sexo not in "MmFf":
        sexo = STRING("😠Dados inválidos!!!\n😬Por favor, informe seu sexo[M/F]:\n>>>").upper()[0]
    if sexo == "M":
        sexo = "HOMEM"
    if sexo == "F":
        sexo = "MULHER"
    print(f"🌝Isso significa que você é {sexo}!!!")
    sleep(3)    
    idade = VALOR_INT("😎Qual é a sua idade?\n>>>")
    if idade <= 30:
        print("😱Nossa,como você é jovem!!!")
    else: 
        print("💪É...Ainda dá pro gasto!")
    sleep(3)    
    mora = STRING("😎Onde você mora?\n>>>").upper()
    if "ACRE" in mora or "SERGIPE" in mora:
        print("🌚Sei,na terra dos dinossauros!")
    elif "BRASIL" in mora or "ARGENTINA" in mora:
        print("😏Sei,no país menos corrupto!")
    else:
        print("🌎Excelente!!!")
    sleep(3)    
    trabalha = STRING("😎Você trabalha em quê?\n>>>").upper()
    if "NÃO" in trabalha or "NAO" in trabalha or "DESEMPREGADO" in trabalha or "DESEMPREGADA" in trabalha or "AUTÔNOMO" in trabalha or "AUTÔNOMA" in trabalha or "AUTONOMO" in trabalha or "AUTONOMA" in trabalha:
        print("😔Com essa crise fica difícil mesmo!")
    else:
        print("🙌Que bom!!!")
    sleep(3)        
    escola = STRING("😎Você tem o ensino médio completo?\n>>>").upper()
    if "SIM" in escola or "TENHO" in escola or "FIZ" in escola or "FACULDADE" in escola or "UNIVERSIDADE" in escola:
        print("👏PARABÉNS!!!")
    elif "NÃO" in escola or "FUNDAMENTAL" in escola:
        print("😔Assim fica complicado️!") 
    else:
        print("👏️Continue,que você consegue!!!️")
    sleep(3)      
    meta = STRING("😎Quais são suas metas para o futuro?\n>>>").upper()
    print("☺️Com estudo e dedicação você consegue!")
    sleep(3)    
    experiência = STRING("😎Agora me conta: Qual é sua experiência profissional?\n>>>").upper()
    if "NÃO" in experiência or "POUCO" in experiência or "POUCA" in experiência or "NENHUM" in experiência or "NENHUMA" in experiência:
        print("😏Nunca é tarde para aprender coisas novas!!!")
    else:
        print("⚡A cada dia; Novo aprendizado!!!")         
    if "MÉDICO" in experiência and meta or "DOUTOR" in experiência and meta or "ADVOGADO" in experiência and meta or "JUIZ" in experiência and meta or "POLÍTICO" in experiência and meta:
        vetor = "👍APROVADO!"
    else:
        vetor = "👎REPROVADO!"                   
    print("😎Agora você irá receber o relatório da entrevista!Aguarde um momento...")
    sleep(2)         
    PROCESSANDO()
    linha(f"  🔰RELATÓRIO FINAL:\n⭐Seu Nome é: {nome}!\n⭐Seu sexo: {sexo}!\n⭐Sua Idade é {idade}!\n⭐Você Mora no: {mora}!\n⭐Seu Trabalho é: {trabalha}!\n⭐Sua Meta é: {meta}!\n⭐Sua Escolaridade (EM): {escola}!\n⭐Sua Experiência é: {experiência}!\n⭐RESULTADO: {vetor}")       
    FIM()