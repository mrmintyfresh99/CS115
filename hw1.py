'''
Created on Sep 12, 2017

@author: mathewseedhom
'''
'''I pledge my honor that I have abided by the Stevens Honor System.
- mseedhom'''

from cs115 import map, reduce

def mult(x, y):
    '''Returns the product of x and y.'''
    return x * y
def factorial(n):
    '''Returns the product of all numbers preceding the input until 0.'''
    return reduce(mult, range(1, n+1))


def add(x, y):
    '''Returns the sum of x and y.'''
    return x + y
def mean(L):
    '''Returns the average of all numbers in the list.'''
    return float(reduce(add, L)/len(L))

def divides(n):
    def div(k):
        return n % k == 0
    return div

def prime(n):
    '''Checks if number n is a prime number.'''
    if n < 2 or sum(map(divides(n), range(2, n))) > 0:
        return False
    return True