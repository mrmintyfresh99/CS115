'''
Created on 10/16/17
@author:   mseedhom
Pledge:    I pledge my honor to have abided by the Stevens Honor System. - mseedhom

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
import string
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.


#The compressed version may be longer than the original due to the padding that is needed to 
#differentiate between the amount of 1's and 0's. For example, if the 64 bit string were just 
#alternating 1's and 0's, the compressed version would actually be much longer. The maximum 
#possible bits a compressed binary string could have would be 325 (5 *65). This would be the
#result if the original string was '10' * 32, because it first checks a zero which would return 5 zeros and 64 '00001'.

#For many of the picture "images", the compression ratio is above 1, meaning that the compressed 
#version actually would take more memory to store, in comparison to the original.

#The only way that it is guaranteed that the compressed string will always be smaller than the 
#original is if the COMPRESSED_BLOCK_SIZE changes between alternations in 1's and 0's. If this 
#were the case, then the compressed string would no longer properly represent an image, due to 
#the image having to be in a rectangular format. If COMPRESSED_BLOCK_SIZE changed every 
#alternation, an irregular shaped image would be created.

def countRun(s, c, maxRun):
    '''param s: a string
    param c: what we're counting
    param maxRun: maximum length of run
    returns: the number of times that string occurs in a row'''
    if s == '':
        return 0
    if s[0] != c:
        return 0
    store = 1 + countRun(s[1:], c, maxRun)
    if store >= maxRun:
        return maxRun
    return store

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 1:
        return True
    return False

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

def compress(s):
    '''Creates a compressed binary string that still represents the original string.'''
    def compressh(s, c):
        if s == '':
            return ''
        runLen = countRun(s, c, MAX_RUN_LENGTH)
        nextC = '0'
        if c == '0':
            nextC = '1'
        return (COMPRESSED_BLOCK_SIZE - len(numToBinary(runLen))) * '0' + numToBinary(runLen) + compressh(s[runLen:], nextC)
    return compressh(s, '0')

def uncompress(s):
    '''Decompresses a compressed binary string into the original string.'''
    def uncompressh(s, c):
        if s == '':
            return ''
        nextC = '0'
        if c == '0':
            nextC = '1'
        return binaryToNum(s[:COMPRESSED_BLOCK_SIZE]) * c + uncompressh(s[COMPRESSED_BLOCK_SIZE:], nextC)
    return uncompressh(s, '0')
    
def compression(s):
    '''Finds the length ratio of the compressed string and the original string.'''
    return len(compress(s)) / len(s)