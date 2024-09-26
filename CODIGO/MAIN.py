from config import *

def main():
    apresentacao()
    opcoes = {
        0: END,
        1: entrevista,
        2: media,
        3: imc,
        4: descontos,
        5: aumentos,
        6: temperatura,
        7: hipotenusa,
        8: sct,
        9: parede,
        10: carros,
        11: radar,
        12: viagem,
        13: bissexto,
        14: emprestimo,
        15: bases_numericas,
        16: militar,
        17: triangulos,
        18: palindromo,
        19: adivinhacao,
        20: pa,
        21: pg,
        22: mmc,
        23: mdc,
        24: primeiro_grau,
        25: segundo_grau,
        26: potenciacao,
        27: tabuada,
        28: tempo,
        29: votacao,
        30: calculadora, 
        31: proporcao,
        32: fracoes,
        33: algebra,
        34: pitagoras,
        35: tales,
        36: reciproco,
        37: cartesiano,
        38: binomio,
        39: polinomio,
        40: trigonometria,
        41: regra_de_tres,
        42: razao,
        43: arquimedes,
        44: poligono,
        45: geometria_plana,
        46: radicais,
        47: conjuntos,
        48: logaritmos,
        49: determinantes,
        50: geometria_analitica
    }

    while True:
        PROCESSO("⌛CARREGANDO", 00, 120, 20, 0.5)     
        LINHA('''   
           MENU PRINCIPAL: \n  
        [ 0 ] SAIR DO PROGRAMA
        [ 1 ] ENTREVISTA COPT
        [ 2 ] CALCULAR A MÉDIA
        [ 3 ] CALCULAR O IMC
        [ 4 ] CALCULAR O DESCONTO
        [ 5 ] CALCULAR O AUMENTO
        [ 6 ] CONVERTER A TEMPERATURA
        [ 7 ] CALCULAR A HIPOTENUSA  
        [ 8 ] CALCULAR SCT
        [ 9 ] PINTAR A PAREDE
        [ 10 ] ALUGUEL DE CARRO
        [ 11 ] RADAR ELETRÔNICO
        [ 12 ] CUSTO DA VIAJEM 
        [ 13 ] ANO BISSEXTO
        [ 14 ] APROVANDO O EMPRÉSTIMO
        [ 15 ] CONVERSOR NUMÉRICO
        [ 16 ] ALISTAMENTO MILITAR
        [ 17 ] ANALISADOR DE TRIÂNGULO
        [ 18 ] DETECTOR DE PALINDROMO
        [ 19 ] JOGO DE ADIVINHAÇÃO
        [ 20 ] PROGRESSÃO ARITMÉTICA (PA)
        [ 21 ] PROGRESSÃO GEOMETRICA (PG)
        [ 22 ] CALCULAR O MMC
        [ 23 ] CALCULAR O MDC
        [ 24 ] EQUAÇÃO DO PRIMEIRO GRAU
        [ 25 ] EQUAÇÃO DO SEGUNDO GRAU
        [ 26 ] POTÊNCIAÇÃO
        [ 27 ] TABUADA
        [ 28 ] CONVERSOR DE TEMPO
        [ 29 ] PODE VOTAR?
        [ 30 ] CALCULADORA 
        [ 31 ] PROPORÇÃO
        [ 32 ] FRAÇÕES
        [ 33 ] ALGEBRA
        [ 34 ] TEOREMA DE PITAGORAS
        [ 35 ] TEOREMA DE TALES
        [ 36 ] TEOREMA RECÍPROCO
        [ 37 ] PLANO CARTESIANO
        [ 38 ] BINÔMIO
        [ 39 ] POLINÔMIO
        [ 40 ] TRIGONOMETRIA
        [ 41 ] REGRA DE TRÊS
        [ 42 ] CALCULAR A RAZÃO
        [ 43 ] ARQUIMEDES
        [ 44 ] POLIGONO
        [ 45 ] GEOMETRIA PLANA
        [ 46 ] RADICAIS
        [ 47 ] DOMINIO E CONJUNTO DE IMAGEM
        [ 48 ] LOGARITMOS
        [ 49 ] DETERMINANTES
        [ 50 ] GEOMETRIA ANALITICA
                 ''')    
        opcao = VALOR_INT("\n😎Digite o número da sua opção:\n>>>") 
        PROCESSO("⌛Carregando", 00, 110, 10, 0.2)
         
        if opcao in opcoes:
            opcoes[opcao]()  
        else:
            print("😠Opção inválida. Tente novamente!")

if __name__ == "__main__":
    main()
