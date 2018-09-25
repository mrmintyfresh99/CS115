'''
Created on Sep 14, 2017

@author: mathewseedhom
'''
'''I pledge my honor that I have abided by the Stevens Honor System.
-mseedhom'''


from cs115 import reduce, filter

def dot(L, K):
    '''This function returns the dot product of list L and K.'''
    def dot_h(L, K, accum):
        if L == [] or K == []:
            return accum
        return dot_h(L[1:], K[1:], L[0] * K[0] + accum)
    return dot_h(L, K, 0)

def explode(S):
    '''This function seperates all the characters of a string.'''
    if S == "":
        return []
    return [S[0]] + explode(S[1:])

def ind(e, L):
    '''This function searches for input e in the list L, and if it is found it outputs where it is in the list. Otherwise it says the length of the list.'''
    if L == "" or L == [] or e == L[0]:
        return 0
    return 1 + ind(e, L[1:])

def removeAll(e, L):
    '''This function searches an element in a list, and produces a new list with none of that element.'''
    def removeAllh(e, L, accum):
        if L == []:
            return accum
        if e == L[0]:
            return removeAllh(e, L[1:], accum)
        return removeAllh(e, L[1:], accum + L[0:1])
    return removeAllh(e, L, [])

def myFilter(f, L):
    '''This function checks the function f on a list, and filters out all the true statements.'''
    if L == []:
        return []
    if f(L[0]) == True:
        return [L[0]] + myFilter(f, L[1:])
    return [] + myFilter(f, L[1:])

def deepReverse(L):
    '''This function reverses the list, and all lists within the list.'''
    if L == []:
        return L
    if isinstance(L[0], list) == True:
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    return deepReverse(L[1:]) + [L[0]]
