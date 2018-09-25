'''
Created on 9/18/17
@author:   mseedhom
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2], ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1], ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1], ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo', 'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
    '''Provides the Scrabble score of the specific letter.'''
    if letter == '' or scorelist == []:
        return 0
    inside = scorelist[0]
    if inside[0] == letter:
        return inside[1]
    return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    '''Provides the Scrabble score of the specific word.'''
    if S == '' or scorelist == []:
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def remove(letter, Rack):
    '''Removes a specific letter within a list of letters.'''
    if Rack == []:
        return []
    if Rack[0] == letter:
        return Rack[1:]
    return [Rack[0]] + remove(letter, Rack[1:])

def checking_that_rack_out(S, Rack):
    '''Checks if a word S could be made from a list of Rack.'''
    if S == '':
        return True
    if S[0] in Rack:
        return checking_that_rack_out(S[1:], remove(S[0], Rack))
    return False

def possiblewords(Rack, Dictionary):
    '''Given a list of Rack, this functions says all the Dictionary words that could be made from it.'''
    return filter(lambda S: checking_that_rack_out(S, Rack), Dictionary)

def scoreList(Rack):
    '''This function outputs all the possible words with their corresponding scores.'''
    words = possiblewords(Rack, Dictionary)
    return map(lambda S: [S, wordScore(S, scrabbleScores)], words)

def bestWord(Rack):
    '''This function determines the word with the highest score from all the words that are able to be produced in the Dictionary.'''
    contenders = scoreList(Rack)
    if contenders == []:
        return ['', 0]
    return reduce((lambda x, y: x if x[1] > y[1] else y), contenders)
