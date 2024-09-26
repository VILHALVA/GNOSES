from config import *

def sct():
    print("😎Irei calcular o seno, cosseno e tangente!")
    sleep(2)        
    ângulo = VALOR_FLOAT("😎Digite o ângulo(ex:30):\n>>>")
    seno = math.sin(math.radians(ângulo))
    cosseno = math.cos(math.radians(ângulo))
    tangente = math.tan(math.radians(ângulo))
    PROCESSANDO()        
    LINHA(f"⚡Com ângulo de {ângulo};\n⭐Ângulo do Seno é: {seno:.2f}!\n⭐Ângulo do Cosseno é: {cosseno:.2f}!\n⭐Ângulo da Tangente é: {tangente:.2f}!")            
    FIM()