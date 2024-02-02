def fracoes():
    from fractions import Fraction
    from time import sleep
    from AAAA import VALOR_INT, PROCESSANDO, linha, FIM

    print("➕ Vamos realizar a adição de duas frações...")
    sleep(3)
    numerador1 = VALOR_INT("➕ Digite o numerador da primeira fração:\n>>>")
    denominador1 = VALOR_INT("➕ Digite o denominador da primeira fração (deve ser diferente de zero):\n>>>")
    numerador2 = VALOR_INT("➕ Digite o numerador da segunda fração:\n>>>")
    denominador2 = VALOR_INT("➕ Digite o denominador da segunda fração (deve ser diferente de zero):\n>>>")
    fracao1 = Fraction(numerador1, denominador1)
    fracao2 = Fraction(numerador2, denominador2)
    resultado = fracao1 + fracao2
    PROCESSANDO()
    linha(f"⚡ A primeira fração é: {fracao1}\n⚡ A segunda fração é: {fracao2}\n⭐ A soma das frações é: {resultado}")

    FIM()

