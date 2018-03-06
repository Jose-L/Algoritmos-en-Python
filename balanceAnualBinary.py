#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 21:56:56 2018

@author: faceless
"""

balance = 999999
annualInterestRate = 0.18


monthlyInterestRate = annualInterestRate/12.0
aux = balance
low = balance /12
high = (balance * (1 + monthlyInterestRate)**12)/12.0
guess = (high + low)/2.0
epsilon=0.01

while(abs(aux)>=epsilon):
    
    aux=balance
    for month in range(1,13):
        monthlyUnpaidBalance = aux - guess
        aux = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
    if aux>0:
        low=guess
    else:
        high=guess
    guess = (high+low)/2.0
    
print('Lowest Payment:',round(guess,2))
