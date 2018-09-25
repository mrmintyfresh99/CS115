'''
Created on 11/21/17
@author:   mseedhom
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. - mseedhom


CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):         
        '''Returns a new object with the same month, day, year            
           as the calling object (self).'''         
        dnew = Date(self.month, self.day, self.year)         
        return dnew 

    def equals(self, d2):         
        '''Decides if self and d2 represent the same calendar date,             
        whether or not they are the in the same place in memory.'''         
        return self.year == d2.year and self.month == d2.month and \
        self.day == d2.day
        
    def tomorrow(self):
        'Says the date of tomorrow.'
        d = Date(self.month, self.day, self.year)
        if self.month == 12 and self.day == 31:
            self.month = 1
            self.day = 1
            self.year += 1
        elif self.month == 2 and self.day == 28 and d.isLeapYear() == True:
            self.day += 1
        elif self.day >= DAYS_IN_MONTH[self.month]:
            self.day = 1
            self.month += 1
        else:
            self.day += 1
    
    def yesterday(self):
        'Says the date of yesterday.'
        d = Date(self.month, self.day, self.year)
        if self.month == 1 and self.day == 1:
            self.month = 12
            self.day = 31
            self.year += -1
        elif self.month == 3 and self.day == 1 and d.isLeapYear() == True:
            self.month = 2
            self.day = 29
        elif self.day == 1:
            self.day = DAYS_IN_MONTH[self.month - 1]
            self.month += -1
        else:
            self.day += -1
            
    def addNDays(self, N):
        'Says the date after N days.'
        for i in range(N):
            print(Date(self.month, self.day, self.year))
            self.tomorrow()
        print(Date(self.month, self.day, self.year))
    
    def subNDays(self, N):
        'Says the date of N days before the date.'
        for i in range(N):
            print(Date(self.month, self.day, self.year))
            self.yesterday()
        print(Date(self.month, self.day, self.year))
    
    def isBefore(self, d2):
        'Says if a date is before another date.'
        if self.year < d2.year:
            return True
        if self.month < d2.month and self.year == d2.year:
            return True
        if self.day < d2.day and self.month == d2.month and self.year == d2.year:
            return True
        return False
    
    def isAfter(self, d2):
        'Says if a date is after another date.'
        if self.equals(d2) == False and self.isBefore(d2) == False:
            return True
        return False
    
    def diff(self, d2):
        'Prints the amount of days between both dates'
        sign = 1
        count = 0
        temp = Date(self.month, self.day, self.year)
        while temp.isBefore(d2):
            count += 1
            sign = -1
            temp.tomorrow()
        while temp.isAfter(d2):
            count += 1
            temp.yesterday()
        return sign * count
    
    def dow(self):
        'Returns what day of the week it is.'
        use = Date(11, 28, 2017)
        if use.isAfter(self):
            if abs(use.diff(self)) % 7 == 0:
                return 'Tuesday'
            elif abs(use.diff(self)) % 7 == 6:
                return 'Wednesday'
            elif abs(use.diff(self)) % 7 == 5:
                return 'Thursday'
            elif abs(use.diff(self)) % 7 == 4:
                return 'Friday'
            elif abs(use.diff(self)) % 7 == 3:
                return 'Saturday'
            elif abs(use.diff(self)) % 7 == 2:
                return 'Sunday'
            return 'Monday'
        if use.isBefore(self):
            if abs(use.diff(self)) % 7 == 0:
                return 'Tuesday'
            elif abs(use.diff(self)) % 7 == 6:
                return 'Monday'
            elif abs(use.diff(self)) % 7 == 5:
                return 'Sunday'
            elif abs(use.diff(self)) % 7 == 4:
                return 'Saturday'
            elif abs(use.diff(self)) % 7 == 3:
                return 'Friday'
            elif abs(use.diff(self)) % 7 == 2:
                return 'Thursday'
            return 'Wednesday'
