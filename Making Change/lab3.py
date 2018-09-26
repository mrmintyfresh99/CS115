'''
Created on Sep 20, 2017

@author: mathewseedhom
'''
'''I have pledged my honor that I have abided by the Stevens Honor System. - mseedhom'''

def change(amount, coins):
    '''This function tells you the least amount of coins needed to make change from a currency.'''
    if amount == 0:
        return 0
    if amount < 0 or coins == []:
        return float('inf')
    if amount == 0 and coins == []:
        return 0
    use_it = change(amount - coins[0], coins) + 1
    lose_it = change(amount, coins[1:])
    return min(use_it, lose_it)
