'''
Created on 10/23/17
@author:   mseedhom
Pledge:    I pledge my honor to have abided by the Stevens Honor System. - mseedhom

CS115 - Hw 7
'''
def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    val = numToBinary(binaryToNum(s) + 1)
    if len(val) > 8:
        return '00000000'
    return '0' * (8-len(val)) + val

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return '00000000'
    if n % 2 == 1:
        value = numToBinary((n-1)/2) + '1'
    if n % 2 == 0:
        value = numToBinary(n/2) + '0'
    if len(value) > 8:
        return value[len(value) - 8:len(value)]
    return (8 - len(value)) * '0' + value

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    return int(s[-1]) + 2 * binaryToNum(s[:-1])

def toggle(S):
    if S == '':
        return ''
    if S[0] == '0':
        return '1' + toggle(S[1:])
    return '0' + toggle (S[1:])


def TcToNum(S):
    'Returns the number that the 8-bit binary string equals.'
    if S[0] == '1':
        return -binaryToNum(increment(toggle(S)))
    return binaryToNum(S)

def NumToTc(n):
    'Returns the 8-bit binary string that the number equals.'
    if n < -128 or n > 127:
        return 'Error'
    if n >= 0:
        return numToBinary(n)
    return increment(toggle(numToBinary(-n)))
