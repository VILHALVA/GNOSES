from config import *

def bases_numericas():
    num = VALOR_INT("😎Digite um número inteiro:\n>>>")
    print("😎Escolha uma das bases para conversão:")       
    LINHA('''
        🎂OPÇÕES:
         [ 1 ] BINÁRIO;
         [ 2 ] OCTAL;
         [ 3 ] HEXADECIMAL;''')
    opção = VALOR_INT("\n😎Escolha a sua opção:\n>>>")
    PROCESSANDO()         
    if opção == 1:
        LINHA(f"⭐Valor: {num:.0f};\n⭐Em BINÁRIO: {bin(num)[2:]}!")
    elif opção == 2:
        LINHA(f"⭐Valor: {num:.0f};\n⭐Em OCTAL: {oct(num)[2:]}!")
    elif opção == 3: 
        LINHA(f"⭐Valor: {num:.0f};\n⭐Em HEXADECIMAL: {hex(num)[2:]}!")
    else:
        LINHA("😡VALOR INVÁLIDO!!!")                                         
    FIM()