#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 21:11:12 2018

@author: faceless
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    '''
    sum = 0
    
    for element in aDict.values():
        sum += len(element)
    return sum
print(how_many(animals))