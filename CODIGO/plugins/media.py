from config import *

def media():
    print("😎Irei calcular as suas 4 notas das provas...")
    sleep(3)    
    nota1 = VALOR_FLOAT("😎Digite a sua 1° Nota da prova:\n>>>")
    nota2 = VALOR_FLOAT("😎Digite a sua 2° Nota da prova:\n>>>")
    nota3 = VALOR_FLOAT("😎Digite a sua 3° Nota da prova:\n>>>")
    nota4 = VALOR_FLOAT("😎Digite a sua 4° Nota da prova:\n>>>")      
    média = (nota1 + nota2 + nota3 + nota4) / 4    
    PROCESSANDO()
    LINHA(f"⚡Sua 1° Nota é: ({nota1:.1f});\n⚡Sua 2° Nota é: ({nota2:.1f});\n⚡Sua 3° Nota é: ({nota3:.1f});\n⚡Sua 4° Nota é: ({nota4:.1f});\n⭐A sua MÉDIA é: ({média:.1f})!")    
    if 7 > média >= 5:
        LINHA("⭐RESULTADO: Você está de RECUPERAÇÃO!")
    elif média < 5:
        LINHA("⭐RESULTADO: Você está REPROVADO!")
    elif média >= 7:
        LINHA("⭐RESULTADO: Você está APROVADO!")       
    FIM() 