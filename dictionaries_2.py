"""
Created on Tue Mar 13 21:22:21 2018

@author: faceless
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it.
    '''
    aux = [];
    for lista in aDict.values():
        aux.append(len(lista))
    maxim = max(aux)
    for key in aDict.keys():
        if maxim == len(aDict[key]):
            return key
