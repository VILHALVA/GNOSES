from config import *

def LINHA(txt):
    print("_" *35)
    print(txt)
    print("_" *35)
      
def PROCESSO(txt, I, F, P, S):
    for c in range(I, F, P):   
        print(f"{txt}({c}%)...", end="\r")
        sleep(S)
        
def PROCESSANDO():
    PROCESSO("⌛PROCESSANDO", 00, 101, 1, 0.1)
    
def VALOR_INT(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("😬ERRO! Digite um valor Inteiro!!!")
            continue
        except KeyboardInterrupt:
            print("🔺Houve erro! Usuário não digitou valor!")
            return n
        else:
            return n 
            
def VALOR_FLOAT(msg):
    while True:
        entrada = input(msg).strip().replace(",", ".")
        if not entrada:
            print("😬ERRO! Valor inválido. Tente novamente.")
            continue
        try:
            valor_float = float(entrada)
            return valor_float
        except ValueError:
            print(f"😬ERRO! \'{entrada}\' é um valor inválido. Tente novamente.")
            
def STRING(msg):
    while True:
        entrada = input(msg).strip()
        if not entrada:
            print("😬ERRO! A string não pode ser vazia. Tente novamente...")
            continue
        if entrada.isnumeric():
            print("😬ERRO! A string não pode ser numérica. Tente novamente...")
            continue
        return entrada 

def FIM():
    sleep(3)
    print("-" *20)
    print("⛔THE END")
    print("-" *20)
    PROCESSO("⌛RENDERIZANDO", 00, 125, 25, 0.4)
    
