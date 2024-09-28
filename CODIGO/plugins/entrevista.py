from config import *

def entrevista():
    print("🔺AVISO: ESSA ENTREVISTA SE TRATA APENAS DE UMA SIMULAÇÃO!!!")
    sleep(3)
    print("😎SEJA BEM-VINDO A MAIS UMA ENTREVISTA GENÉRICA.")
    sleep(3)   
    
    NOME = STRING("😎QUAL É O SEU NOME?\n>>> ").upper()
    if any(x in NOME for x in ["SAMUEL", "DANIEL", "LUCAS", "MARIA", "ANA"]):
        print("😍QUE NOME LINDO VOCÊ TEM!")
    else: 
        print("😒SEU NOME É TÃO COMUM!")
    sleep(3)
    
    SEXO = STRING("😎INFORME O SEU SEXO [M/F]:\n>>> ").upper()[0]
    while SEXO not in "MF":
        SEXO = STRING("😠DADOS INVÁLIDOS!!!\n😬POR FAVOR, INFORME SEU SEXO [M/F]:\n>>> ").upper()[0]
    
    SEXO = "HOMEM" if SEXO == "M" else "MULHER"
    print(f"🌝ISSO SIGNIFICA QUE VOCÊ É {SEXO}!!!")
    sleep(3)
    
    IDADE = VALOR_INT("😎QUAL É A SUA IDADE?\n>>> ")
    print("😱NOSSA, COMO VOCÊ É JOVEM!!!" if IDADE <= 30 else "💪É... AINDA DÁ PRO GASTO!")
    sleep(3)
    
    LOCAL = STRING("😎ONDE VOCÊ MORA?\n>>> ").upper()
    if any(x in LOCAL for x in ["ACRE", "SERGIPE"]):
        print("🌚SEI, NA TERRA DOS DINOSSAUROS!")
    elif any(x in LOCAL for x in ["BRASIL", "ARGENTINA"]):
        print("😏SEI, NO PAÍS MENOS CORRUPTO!")
    else:
        print("🌎EXCELENTE!!!")
    sleep(3)
    
    TRABALHO = STRING("😎VOCÊ TRABALHA EM QUÊ?\n>>> ").upper()
    if any(x in TRABALHO for x in ["NÃO", "NAO", "DESEMPREGADO", "DESEMPREGADA", "AUTÔNOMO", "AUTÔNOMA", "AUTONOMO", "AUTONOMA"]):
        print("😔COM ESSA CRISE FICA DIFÍCIL MESMO!")
    else:
        print("🙌QUE BOM!!!")
    sleep(3)
    
    ESCOLA = STRING("😎VOCÊ TEM O ENSINO MÉDIO COMPLETO? (RESPOSTA: SIM, NÃO, FACULDADE, UNIVERSIDADE, FUNDAMENTAL)\n>>> ").upper()
    if any(x in ESCOLA for x in ["SIM", "TENHO", "FIZ", "ENSINO MÉDIO", "ENSINO MEDIO"]):
        print("👏PARABÉNS! VOCÊ TEM O ENSINO MÉDIO COMPLETO.")
        ESCOLARIDADE = "ENSINO MÉDIO COMPLETO"
    elif any(x in ESCOLA for x in ["FACULDADE", "UNIVERSIDADE"]):
        print("👏PARABÉNS! VOCÊ TEM NÍVEL SUPERIOR.")
        ESCOLARIDADE = "NÍVEL SUPERIOR"
    elif any(x in ESCOLA for x in ["NÃO", "NAO", "FUNDAMENTAL"]):
        print("😔ASSIM FICA COMPLICADO!")
        ESCOLARIDADE = "ENSINO FUNDAMENTAL INCOMPLETO"
    else:
        print("👏CONTINUE, QUE VOCÊ CONSEGUE!!!")
        ESCOLARIDADE = "OUTRO NÍVEL EDUCACIONAL"
    sleep(3)
    
    META = STRING("😎QUAIS SÃO SUAS METAS PARA O FUTURO?\n>>> ").upper()
    print("☺️COM ESTUDO E DEDICAÇÃO VOCÊ CONSEGUE!")
    sleep(3)
    
    EXPERIENCIA = STRING("😎AGORA ME CONTA: QUAL É SUA EXPERIÊNCIA PROFISSIONAL?\n>>> ").upper()
    if any(x in EXPERIENCIA for x in ["NÃO", "NAO", "POUCO", "POUCA", "NENHUM", "NENHUMA"]):
        print("😏NUNCA É TARDE PARA APRENDER COISAS NOVAS!!!")
    else:
        print("⚡A CADA DIA; NOVO APRENDIZADO!!!")
    
    if any(x in EXPERIENCIA for x in ["MÉDICO", "DOUTOR", "ADVOGADO", "JUIZ", "POLÍTICO"]) and META:
        RESULTADO = "👍APROVADO!"
    else:
        RESULTADO = "👎REPROVADO!"
    
    print("😎AGORA VOCÊ IRÁ RECEBER O RELATÓRIO DA ENTREVISTA! AGUARDE UM MOMENTO...")
    sleep(2)
    PROCESSANDO()
    
    TEMPO = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    RES = f'''
    =========================================
        🔰RELATÓRIO FINAL:
    -----------------------------------------
    ⭐TIME -> {TEMPO}
    ⭐SEU NOME -> {NOME}
    ⭐SEU SEXO -> {SEXO}
    ⭐SUA IDADE -> {IDADE} ANOS
    ⭐VOCÊ MORA -> {LOCAL}
    ⭐SEU TRABALHO -> {TRABALHO}
    ⭐SUA META -> {META}
    ⭐SUA ESCOLARIDADE -> {ESCOLARIDADE}
    ⭐SUA EXPERIÊNCIA -> {EXPERIENCIA}
    ⭐RESULTADO => {RESULTADO}
    -----------------------------------------
    ==========================================
    '''
    print(RES)
    sleep(3)
    
    SALVAR = input("😃VOCÊ DESEJA SALVAR ESSE RELATÓRIO FINAL? ENVIE 'S' PARA CONFIRMAR!:\n>>> ").strip().upper()
    
    if SALVAR == "S":
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        FILES_DIR = os.path.join(BASE_DIR, 'files')
        
        if not os.path.exists(FILES_DIR):
            os.makedirs(FILES_DIR)
        
        TEMPO_FORMATADO = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        FILE_NAME = f"GNOSES_{TEMPO_FORMATADO}.txt"
        FILE_PATH = os.path.join(FILES_DIR, FILE_NAME)
        
        with open(FILE_PATH, 'a', encoding='utf-8') as FILE:
            FILE.write(RES)
        
        print(f"😃O RELATÓRIO FINAL FOI SALVO COM SUCESSO EM '{FILE_PATH}'!")
        sleep(3)
    else:
        print("🤨TUDO BEM. O RELATÓRIO FINAL NÃO FOI SALVO!")
        sleep(3)
    
    FIM()
