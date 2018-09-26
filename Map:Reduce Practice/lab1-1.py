'''
Created on Sep 8, 2017

@author: mathewseedhom
'''

'''I pledge my honor that I have abided by the Stevens Honor System'''

from math import factorial
import math

def inverse(n):
    '''This function returns the reciprocal of the input.'''
    return 1 / n

def e(n):
    '''This function returns the approximated value of e based on n iterations.'''
    return(sum(map(inverse, map(factorial, range(1, n+1)))) + 1)

def error(n):
    '''This function returns the difference between the approximate of e and the true value of e.'''
    return(abs(math.e - e(n)))