'''
Created on 10/23/17
@author:   mseedhom
Pledge:    I pledge my honor to have abided by the Stevens Honor System. - mseedhom

CS115 - Hw 7
'''

def numToBaseB(N, B):
    'Converts the number N in base 10 into a string in base B (from bases 2 - 10).'
    if N == 0:
        return '0'
    def numToBaseBh(N, B):
        if N == 0:
            return '' 
        return numToBaseBh(N // B, B) + str(N % B)
    return numToBaseBh(N, B)

def baseBToNum(S, B):
    'Converts a string in base B (from bases 2 - 10) into a number in base 10.'
    if S == '':
        return 0
    return int(S[-1]) + B *  baseBToNum(S[:-1], B)

def baseToBase(B1,B2,SinB1):
    'Converts a string of base B1 into a string of base B2.'
    return numToBaseB(baseBToNum(SinB1, B1), B2)

def add(S,T):
    'Adds 2 strings in binary by converting to base 10 first.'
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)

FullAdder = \
{ ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

def addB(S, T):
    'Adds 2 strings of binary using binary addition rules.'
    def addBh(S, T, carry):
        if S == '' and T == '' and carry == '0':
            return ''
        if S == '' and T == '':
            sumBit, carryBit = FullAdder[('0', '0', carry)]
        elif S == '':
            sumBit, carryBit = FullAdder[('0', T[-1], carry)]
        elif T == '':
            sumBit, carryBit = FullAdder[(S[-1], '0', carry)]
        else:
            sumBit, carryBit = FullAdder[(S[-1],T[-1], carry)] 
        answer = addBh(S[:-1], T[:-1], carryBit) + sumBit
        if answer[0] == '0':
            answer = answer[1:]
        return answer
    return addBh(S, T, '0')
print(addB('000001', '1'))
