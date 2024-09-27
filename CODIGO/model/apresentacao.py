from config import *

def apresentacao():
    ascii_art = pyfiglet.figlet_format("GNOSES")
    print(ascii_art)
    sleep(2)
    cont = 1
    def tempo(txt1, segundos, txt2):
        print(f"😠FORAM {cont} TENTATIVAS!!!", end="\r")
        sleep(2)
        for c in range(segundos, 0, -1):
            print(f"{txt1}: {c} {txt2}", end="\r")
            sleep(1)
    senha = STRING("😎DIGITE A SENHA PARA COMEÇAR:\n>>>")
    while senha not in "VILHALVA":
        cont += 1
        senha = STRING("😎SENHA INVÁLIDA!!! TENTE NOVAMENTE:\n>>>")
        if cont == 3:
            tempo("⌛AGUARDE", 60, "SEGUNDOS...")
        elif cont == 6:
            tempo("⌛AGUARDE", 300, "SEGUNDOS...")
        elif cont > 10:
            tempo("⌛AGUARDE", 9999999, "SEGUNDOS...")
    print("=" * 35, f"\n👏PARABÉNS!!!\n🔓VOCÊ ACERTOU!!!\n⭐Foram {cont} tentativas!!!\n", "=" * 35)
    sleep(2)
    PROCESSO("⌛INICIANDO", 00, 110, 10, 0.7)
    name = STRING("👽PARA COMEÇARMOS, POR FAVOR, DIGITE O SEU NOME:\n>>>")
    print(f"🌞SEJA BEM VINDO AO GNOSES, {name}. ESSE BOT FOI CRIADO PARA RESOLVER PEQUENOS PROBLEMAS!")
    sleep(1)
    print("😎ESSE BOT FOI CRIADO PELO SAMUEL MARTINS VILHALVA -> 🐱GITHUB: @VILHALVA")
    sleep(3)
    print("⏬VOCÊ IRÁ RECEBER O MENU DE OPÇÕES LOGO ABAIXO. BASTA DIGITAR O NÚMERO DA FUNÇÃO QUE VOCÊ DESEJA USAR:")


