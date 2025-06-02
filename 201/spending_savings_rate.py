#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:40:43 2022

@author: kali


Take in two numbers, the first number is how much 
someone spends a month, 
and the second is how much someone earns a month. 

Output the individual's savings and spending rates as: 
    "Your spending rate is <Spending Rate>% and 
    your savings rate is <Savings Rate Here>%". 
    Both rates will be output as a percentage. 

Spending rate = Spending/income 

Savings rate = Savings/income

"""

#1. Crear funcion. 
#2. Recibir inputs as integers
# crear spendin rate
#crea saving
# crear saving_rates
# retornar funcion
# convertir retornos en string
# agregar signos 
#llamar e imprimir la funcion

def spending_saving(spend, income):
    spending_rate =(spend/income) *100
    savings = (income-spend)
    saving_rates = (savings/income) * 100
    return ("Your spending rate is " + 
            str(spending_rate) +
           "% and your savings rate is "
           + str(saving_rates) +"%")

spending, saving = int(input()), int(input())


print (spending_saving(spending, saving))