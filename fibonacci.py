# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:45:28 2019

@author: RLARIOS
"""
#%%

def fib(n):    # Imprime la serie de fibonnaci hasta el número n
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a+b
    print()



def fib2(n):   # retorna la serie de fibonacci en cada posición hasta n
    result = []
    a, b = 0, 1
    while a <= n:
        result.append(a)
        a, b = b, a+b
    return result


def suma_en_fibo( x , y ):
    print( x + y )


