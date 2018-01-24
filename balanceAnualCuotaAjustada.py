#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:46:46 2018
Programa para calcular la cuota minima ajustada (multiplo de 10) dentro de un rango de
12 meses

@author: faceless
"""

balance = 3809
annualInterestRate = 0.04
minimunFixedPayment = 0
monthlyInterestRate = annualInterestRate/12.0
aux = balance
while(aux>0):
    minimunFixedPayment+=10
    aux=balance
    for month in range(1,13):
        monthlyUnpaidBalance = aux - minimunFixedPayment
        aux = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
print('Lowest Payment:',minimunFixedPayment)

    