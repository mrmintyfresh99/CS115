'''
Created on 10/6/17
@author:   mseedhom
Pledge:    I pledge my honor to have abided by the Stevens Honor System. - mseedhom

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 1:
        return True
    return False
#If n is odd the rightmost bit is 1. If n is even the rightmost bit is 0.

#Removing the rightmost bit would be doing a floor division by 2 (n // 2).

#If N is odd all you would have to do is take the base-2 representation of Y and add a 1 
#   to the right, essentially reversing the floor division.

#If N is even all you would have to do is take the base-2 representation of Y and add a 0 
#   to the right, essentially reversing the floor division.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if isOdd(n) == True:
        return numToBinary((n-1)/2) + '1'
    return numToBinary(n/2) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    return int(s[-1]) + 2 * binaryToNum(s[:-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    val = numToBinary(binaryToNum(s) + 1)
    if len(val) > 8:
        return '00000000'
    return '0' * (8-len(val)) + val

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n < 0:
        return ''
    print(s)
    return count(increment(s), n - 1)

#59 in ternary would be 2012. This is because 2(3 ** 0) + 1(3 ** 1) + 0(3 ** 2) + 2(3 ** 3) = 59.

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    return numToTernary(n // 3) + str(n % 3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    return int(s[-1]) + 3 *  ternaryToNum(s[:-1])
