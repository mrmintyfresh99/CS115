'''
Created on 11/16/17
@author:   mseedhom
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. - mseedhom

CS115 - Lab 11
'''

class QuadraticEquation(object):
    
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        
    @property
    def a(self):
        return self.__a
    
    @property
    def b(self):
        return self.__b
    
    @property
    def c(self):
        return self.__c
    
    def discriminant(self):
        return self.__b ** 2 - 4 * self.__a * self.__c
    
    def root1(self):
        if  self.discriminant() < 0:
            return None
        return (-self.__b + self.discriminant() ** .5) / (2 * self.__a)
    
    def root2(self):
        if  self.discriminant() < 0:
            return None
        return (-self.__b - self.discriminant() ** .5) / (2 * self.__a)
    
    def __str__(self):
        if self.__a == 1:
            a = 'x^2' 
        if self.__a == -1:
            a = '-x^2' 
        elif self.__a > 0 and self.__a != 1:
            a = str(self.__a) + 'x^2'
        elif self.__a < 0 and self.__a != -1:
            a = '-' + str(abs(self.__a)) + 'x^2'
            
        if self.__b == 1:
            b = ' + x'
        if self.__b == -1:
            b = ' - x'
        if self.__b == 0:
            b = ''
        elif self.__b > 0 and self.__b != 1:
            b = ' + ' + str(self.__b) + 'x'
        elif self.__b < 0 and self.__b != -1:
            b = ' - ' + str(abs(self.__b)) + 'x'
            
        if self.__c == 0:
            c = ''
        elif self.__c > 0:
            c = ' + ' + str(self.__c)
        else:
            c = ' - ' + str(abs(self.__c))
        s = a + b + c + ' = 0'
        return s