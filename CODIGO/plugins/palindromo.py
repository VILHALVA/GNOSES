from config import *

def palindromo():
    frase = STRING("😎Digite uma frase:\n>>>").upper()
    palavras = frase.split()
    junto = "*".join(palavras)
    inverso = " "
    PROCESSANDO()
    for letra in range(len(junto) -1, -1, -1):
        inverso += junto[letra]
    if inverso == junto:
        resultado = "👍SIM!!!"
    else:
        resultado = "👎NÃO!!!"         
    LINHA(f"⭐Você inscreveu: {junto}!\n⭐Inverso é {inverso}!\n⭐É Palíndromo?:{resultado}")         
    FIM()