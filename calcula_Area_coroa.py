# -*- coding: utf-8 -*-
def calcula_area(r):
    """Calcula a area"""
    return 3.14*r**2

def area_coroa(r1, r2):
    """Calcula a área da cora"""
    return calcula_area(r1) - calcula_area(r2)

r1 = input("digite r1: ")
r2 = input ("digite r2: ")
ac = area_coroa(r1, r2)

print("Resultado área da coroa: ", ac)
