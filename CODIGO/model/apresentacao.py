from config import *

def apresentacao():
    cont = 1
    def tempo(txt1, segundos, txt2):
        print(f"😠Foram {cont} tentativas!!!", end="\r")
        sleep(2)
        for c in range(segundos, 0, -1):
            print(f"{txt1}: {c} {txt2}", end="\r")
            sleep(1)
    senha = STRING("😎Digite a senha para começar:\n>>>")
    while senha not in "VILHALVA":
        cont += 1
        senha = STRING("😎Senha inválida!!! Tente novamente:\n>>>")
        if cont == 3:
            tempo("⌛AGUARDE", 60, "SEGUNDOS...")
        elif cont == 6:
            tempo("⌛AGUARDE", 300, "SEGUNDOS...")
        elif cont > 10:
            tempo("⌛AGUARDE", 9999999, "SEGUNDOS...")
    print("=" * 35, f"\n👏PARABÉNS!!!\n🔓VOCÊ ACERTOU!!!\n⭐Foram {cont} tentativas!!!\n", "=" * 35)
    sleep(2)
    PROCESSO("⌛INICIANDO", 00, 110, 10, 0.7)
    name = STRING("👽Para começarmos, por favor, digite o seu nome:\n>>>")
    print(f"🌞Seja bem vindo ao Gnoses, {name}. Esse programa foi criado para resolver pequenos problemas!")
    sleep(1)
    print("😎ESSE BOT FOI CRIADO PELO SAMUEL MARTINS VILHALVA -> 🐱GITHUB: @VILHALVA")
    sleep(3)
    print("⏬Você irá receber o menu de opções logo abaixo. Basta digitar o número da função que você deseja usar:")


