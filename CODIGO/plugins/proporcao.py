from config import *

def proporcao():
    print("🔄 Vamos calcular a proporção entre dois valores...")
    sleep(3)
    valor1 = VALOR_FLOAT("🔄Digite o primeiro valor:\n>>>")
    valor2 = VALOR_FLOAT("🔄Digite o segundo valor:\n>>>")
    if valor2 != 0:
        proporcao = valor1 / valor2
        PROCESSANDO()
        LINHA(f"⚡ O primeiro valor é: ({valor1:.2f})\n⚡ O segundo valor é: ({valor2:.2f})\n⭐ A proporção é: ({proporcao:.2f})")
    else:
        LINHA("⚠️Erro: Não é possível calcular a proporção quando o segundo valor é zero!")

    FIM()


