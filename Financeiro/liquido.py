# -*- coding: utf-8 -*-
def calculo_inss(salario):
    #Calcula do INSS
    if salario <= 1000.0:
        return 0.0
    if salario <= 2000.0:
        return salario*0.1
    else:
        return salario*0.2

def calculo_IR(salario_base):
    #Calculo do IR
    if salario_base <= 1400.0:
        return 0.0
    elif salario_base <= 2500.0:
        return salario_base*0.12
    elif salario_base <= 5000.0:
            return salario_base*0.2
    else:
        return salario_base*0.27

def calculo_salario_liquido(salario, dependente):
    #Calculo do salário líquido
    inss = calculo_inss(salario)
    salario_ir = salario - inss - 100.0*dependente
    IR = calculo_IR(salario_ir)
    return salario - inss - IR

salario = float (input ("Digite o seu salário: "))
dependente = int (input ("Digite o número de dependentes: "))

print calculo_salario_liquido(salario, dependente)
