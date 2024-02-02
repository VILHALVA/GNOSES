def temperatura():
    from time import sleep
    from AAAA import VALOR_FLOAT, VALOR_INT, PROCESSANDO, linha, FIM

    print("😎Esse é um programa para Conversão de Temperaturas!(C°/F°/K°)")
    sleep(3)
    linha("📤Envie 1 para converter de Celsius para Fahrenheit;\n📥Envie 2 para converter de Fahrenheit para Celsius;\n🔄Envie 3 para converter de Celsius para Kelvin;\n🔄Envie 4 para converter de Fahrenheit para Kelvin!")
    sleep(3)
    escolha = VALOR_INT("😎Escolha o tipo de conversão que deseja realizar:\n>>>")
    if escolha in [1, 2, 3, 4]:
        temperatura_input = VALOR_FLOAT("😎Agora digite a temperatura a ser convertida:\n>>>")
        if escolha == 1:
            F = temperatura_input * (9 / 5) + 32
            PROCESSANDO()
            linha(f"⚡Convertendo: {temperatura_input:.2f}°C!\n⭐Valor em Fahrenheit é {F:.2f}°F!")
        elif escolha == 2:
            C = (temperatura_input - 32) * (5 / 9)
            PROCESSANDO()
            linha(f"⚡Convertendo: {temperatura_input:.2f}°F!\n⭐Valor em Celsius é {C:.2f}°C!")
        elif escolha == 3:
            K = temperatura_input + 273.15
            PROCESSANDO()
            linha(f"⚡Convertendo: {temperatura_input:.2f}°C!\n⭐Valor em Kelvin é {K:.2f}K!")
        elif escolha == 4:
            K = (temperatura_input + 459.67) * (5 / 9)
            PROCESSANDO()
            linha(f"⚡Convertendo: {temperatura_input:.2f}°F!\n⭐Valor em Kelvin é {K:.2f}K!")
    else:
        print("😠Valor inválido. Tente novamente!!!")
    FIM()


