'''
Created on Oct 2, 2017

@author: mathewseedhom

I pledge my honor that I have abided by the Stevens Honor System. - mseedhom
CS115-A
'''

def pascal_row(n):
    'Returns the nth term of the Pascal triangle.'
    def pascal_h(lst):
        if lst == [1]:
            return []
        return [lst[0]+lst[1]] + pascal_h(lst[1:])
    if n == 0:
        return [1]
    return [1] + pascal_h(pascal_row(n-1)) + [1]

def pascal_triangle(n):
    'Returns all terms in the Pascal Triangle up to the nth term.'
    if n == 0:
        return [[1]]
    return pascal_triangle(n-1) + [pascal_row(n)]
