from time import sleep, time as datetime  
from random import randint
import pyfiglet
import math
import os
from datetime import datetime
from math import comb
import numpy as np
from fractions import Fraction

from model.central import (
    LINHA, 
    PROCESSO, 
    PROCESSANDO, 
    FIM, 
    VALOR_INT, 
    VALOR_FLOAT, 
    STRING, 
    FIM
)

from model.apresentacao import apresentacao
from model.final import final
from plugins.entrevista import entrevista
from plugins.adivinhacao import adivinhacao
from plugins.entrevista import entrevista
from plugins.media import media
from plugins.imc import imc
from plugins.descontos import descontos
from plugins.aumentos import aumentos
from plugins.temperaturas import temperatura
from plugins.hipotenusa import hipotenusa
from plugins.sct import sct
from plugins.parede import parede
from plugins.carros import carros
from plugins.radar import radar
from plugins.viagem import viagem
from plugins.bissexto import bissexto
from plugins.emprestimo import emprestimo
from plugins.bases_numericas import bases_numericas
from plugins.militar import militar
from plugins.triangulos import triangulos
from plugins.palindromo import palindromo
from plugins.adivinhacao import adivinhacao
from plugins.pa import pa
from plugins.pg import pg
from plugins.mmc import mmc
from plugins.mdc import mdc
from plugins.primeiro_grau import primeiro_grau
from plugins.segundo_grau import segundo_grau
from plugins.potenciacao import potenciacao
from plugins.tabuada import tabuada
from plugins.tempo import tempo
from plugins.votacao import votacao
from plugins.calculadora import calculadora
from plugins.proporcao import proporcao
from plugins.fracoes import fracoes
from plugins.algebra import algebra
from plugins.pitagoras import pitagoras
from plugins.tales import tales
from plugins.reciproco import reciproco
from plugins.cartesiano import cartesiano
from plugins.binomio import binomio
from plugins.polinomio import polinomio
from plugins.trigonometria import trigonometria
from plugins.regra_de_tres import regra_de_tres
from plugins.razao import razao
from plugins.arquimedes import arquimedes
from plugins.poligono import poligono
from plugins.geometria_plana import geometria_plana
from plugins.radicais import radicais
from plugins.conjuntos import conjuntos
from plugins.logaritmos import logaritmos
from plugins.determinantes import determinantes
from plugins.geometria_analitica import geometria_analitica
