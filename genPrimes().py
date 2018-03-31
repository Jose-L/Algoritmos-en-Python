"""
Created on Fri Mar 30 20:19:21 2018

@author: faceless
"""
def genPrimes():
    primeList = []
    primeList.append(2)
    yield primeList[-1]
    primeList.append(3)
    yield primeList[-1]
    nextNum = 4
    while True:
        flag = True
        nextNum = nextNum+1
        for n in range(2,nextNum):
            if nextNum % n == 0:
                flag = False
                break
        if flag:
            primeList.append(nextNum)
            yield primeList[-1]
