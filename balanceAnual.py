#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:45:02 2018
Algoritmo para calcular el balance anual si se paga la cuota mínima; Le va
sumando el interés compuesto.
@author: faceless
"""
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

minimunPayment= 0
for month in range(1,13):
    minimunPayment = balance*monthlyPaymentRate
    balance = (balance-minimunPayment)+(balance-minimunPayment)*(annualInterestRate/12.0)
print('Remaining balance: ',round(balance,2))
    