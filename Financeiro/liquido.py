# -*- coding: utf-8 -*-
def calculo_inss(salario):
  return (salario * 20)/100

def calculo_IR(salario, dependente):
    inss = calculo_inss(salario)
    desconto_depen = dependente*100.00
    return salario - inss - desconto_depen

salario = input ("Digite o seu salário: ")
dependente = input ("Digite o número de dependentes: ")

print calculo_IR(salario, dependente)
