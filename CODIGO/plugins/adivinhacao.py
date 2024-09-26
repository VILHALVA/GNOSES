from config import *

def adivinhacao():
    computador = randint(0,10)
    print("😠Acabei de pensar em um número entre 0 e 10!")
    sleep(2)
    acertou = False
    palpites = 0
    while not acertou:
        jogador = VALOR_INT("😎Qual é o seu palpite?:\n>>>")
        palpites += 1
        PROCESSANDO()
        if jogador == computador:
            acertou = True
            resultado = f"👍ACERTOU!\n🔔Foram {palpites} Tentativas!"
        else:
            if jogador < computador:
                     LINHA(f"👎ERRADO!\n➕É MAIOR DO QUE {jogador}!")
            elif jogador > computador:
                LINHA(f"👎ERRADO!\n➖É MENOR QUÊ {jogador}!!!")            
    LINHA(f"⭐Eu pensei no n° {computador}!\n⭐Você digitou: {jogador}!\n⭐RESULTADO:{resultado}")        
    FIM()