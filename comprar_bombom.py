# -*- coding: utf-8 -*-
def calcula_bombom (dinheiro, preco):
    """ Calcula o numero de bombons e o troco, respectivamente"""
    num_bombons = int(dinheiro / preco)
    troco = dinheiro - num_bombons * preco
    return num_bombons, troco

preco = input ("Digite o valor dos bombons: ")
dinheiro =input ("Digite quanto Joaozinho tem: ")
bombons, troco = calcula_bombom (dinheiro, preco)

print  "O número de bombons é: ", bombons
print  "O número de troco é: ", troco
