#
# life.py - Game of Life lab
#
# Name:
# Pledge:
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """ 
    A = []
    for row in range(height):
        A += [width * [0]]    
    return A

def printBoard( A ):
    """ this function prints the 2d list-of-lists
        A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width,height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    'Creates an empty board then modifies the interior to be live.'
    A = createBoard( w, h )
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = 1
    return A

def randomCells(w,h):
    'Creates an empty board then modifies the random cells in the interior to be live.'
    A = createBoard( w, h )
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = random.choice([0, 1])
    return A

def copy(A):
    'Creates a deep copy of an old array.'
    newA = []
    for x in A:
        if isinstance(x, list):
            newA.append(copy(x))
        else:
            newA.append(x)
    return newA
    
def innerReverse(A):
    'Reverses the interior of a copy of A'
    newA = copy(A)
    for row in range(1, len(A) - 1):
        for col in range(1, len(A[0]) - 1):
            if newA[row][col] == 0:
                newA[row][col] = 1
            else:
                newA[row][col] = 0
    return newA

def countNeighbors(row, col, A):
    'Returns the amount of live neighbors around a cell in A'
    count = 0
    if A[row][col] == 1:
        count = -1
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if A[r][c] == 1:
                count += 1
    return count

def next_life_generation(A):
    """ makes a copy of A and then advanced one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays 0.
    """     
    newA = copy(A)
    for row in range(1, len(A) - 1):
        for col in range(1, len(A[0]) - 1):
            if A[row][col] == 0 and countNeighbors(row, col, A) == 3:
                newA[row][col] = 1
            if A[row][col] == 1 and countNeighbors(row, col, A) < 2:
                newA[row][col] = 0
            if A[row][col] == 1 and countNeighbors(row, col, A) > 3:
                newA[row][col] = 0
            if A[row][col] == 1 and countNeighbors(row, col, A) == 2:
                newA[row][col] = 1
            if A[row][col] == 0 and countNeighbors(row, col, A) == 2:
                newA[row][col] = 0
    return newA
