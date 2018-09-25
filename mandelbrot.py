'''
Created on 11/3/17
@author:   mseedhom
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. - mseedhom

CS115 - Lab 9
'''

# keep this import line...
from cs5png import *

# start your Lab 9 functions here:

def mult( c, n ):
    """ mult uses only a loop and addition
    to multiply c by the integer n"""
    result = 0
    for x in range( n ):
        result += c
    return result

def update( c, n ):
    """ update starts with z=0 and runs z = z**2 + c
    for a total of n times. It returns the final z."""
    z = 0
    for x in range(n):
        z = z * z + c
    return z

def inMSet(c, n):
    """ inMSet takes in
    c for the update step of z = z**2+c
    n, the maximum number of times to run that step
    Then, it should return
    False as soon as abs(z) gets larger than 2
    True if abs(z) never gets larger than 2 (for n iterations)"""
    z = 0
    for x in range(n):
        z = z * z + c
        if abs(z) > 2:
            return False
    return True

def weWantThisPixel( col, row ):
    """ a function that returns True if we want
    the pixel at col, row and False otherwise"""
    if col%10 == 0  or  row%10 == 0:
        return True
    else:
        return False
def test():
    """ a function to demonstrate how
     to create and save a png image"""
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()
test()
#It would no longer create points, but instead create lines because it would return points that only has to satisfy one of the criteria.
#This means that it would print the lines x = 0, 10, 20, 30, ..., 300 and y = 0, 10, 20, 30, ..., 200.

def scale(pix, pixMax, floatMin, floatMax):
    """ scale takes in
    pix, the CURRENT pixel column (or row)
    pixMax, the total # of pixel columns
    floatMin, the min floating-point value
    floatMax, the max floating-point value
    scale returns the floating-point value that corresponds to pix"""
    return  floatMin + (floatMax - floatMin) *  pix / pixMax

def mset():
    """ creates a 300x200 image of the Mandelbrot set
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            # here is where you will need
            # to create the complex number, c!
            x = scale(col, 300, -2, 1)
            y = scale(row, 200, -1, 1)
            c = x + y*1j
            if inMSet( c, 25 ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()
mset()