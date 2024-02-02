def reciproco():   
    from time import sleep
    from AAAA import VALOR_FLOAT, PROCESSANDO, linha, FIM
    
    print("🔍Vamos verificar o Teorema Recíproco de Tales!")
    sleep(2)
    ponto_intersecao = VALOR_FLOAT("📍Digite o ponto de interseção nas duas retas não paralelas:\n>>>")
    razao_paralelas = VALOR_FLOAT("🔍 Digite a razão entre os segmentos nas três retas paralelas:\n>>>")
    if ponto_intersecao == razao_paralelas:
        PROCESSANDO()
        linha(f"⚡O ponto de interseção nas duas retas não paralelas é: {ponto_intersecao}\n⚡A razão entre os segmentos nas três retas paralelas é: {razao_paralelas}\n⭐As retas cortam nas mesmas razões. O Teorema Recíproco de Tales é verificado!")
    else:
        PROCESSANDO()
        linha(f"⚡ O ponto de interseção nas duas retas não paralelas é: {ponto_intersecao}\n⚡ A razão entre os segmentos nas três retas paralelas é: {razao_paralelas}\n⛔ As retas não cortam nas mesmas razões. O Teorema Recíproco de Tales não é verificado.")

    FIM()

