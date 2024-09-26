from config import *

def parede():
    print("🌝Irei fazer o cálculo para descobrir a quantidade de litros de tinta para você pintar a sua parede!")
    sleep(3)
    base = VALOR_FLOAT("😎Digite a largura da parede(m):\n>>")
    altura = VALOR_FLOAT("😎Digite a altura da parede(m):\n>>>")
    área = base * altura
    tinta = área / 2
    PROCESSANDO()         
    LINHA(f"⚡Sua dimensão é ({base:.0f})m × ({altura:.0f})m!\n⚡Para pintar a parede de {área:.0f}m²;\n⭐Precisará usar {tinta:.2f}L de tinta!")         
    FIM()
    
    