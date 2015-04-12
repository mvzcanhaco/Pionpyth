'''
Created on 08/04/2015

@author: Marcus
'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# programa1.py - Primeiro Programa
#programa jogo de adivinhação de numeros

import random
numero = random.randint(1,100)
escolha = 0
tentativas = 0
while escolha != numero:
    escolha = input("Escolha um numero entre 1 a 100:")
    tentativas +=1
    if escolha < numero:
        print "O numero", escolha, "e menor que o sorteado."
    elif escolha > numero:
        print "O numero", escolha, "e maior que o sorteado"
print "Parabens! Voce acertou com", tentativas, "tentativas."