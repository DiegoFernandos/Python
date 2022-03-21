# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:07:15 2022

@author: DTIC
"""

testYears = [1900, 2000, 2016, 1987]
testMonths = [ 2, 2, 1, 11]
testResults = [28, 29, 31, 30]
def leapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
 
def monthYear(year, monthNumber):
    if year <= 1582:
        return print(f'{year} - {None} - The leap year is not delclared.')
    elif monthNumber <= 0 or monthNumber > 13:
        return print(f'{monthNumber} - {None} - The number of the month must be between 1 and 12')
    else:
        numberOfDaysPerMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
        res = numberOfDaysPerMonth[monthNumber-1]
        if monthNumber == 2 and leapYear(year) == True:
            res = 29
        return res
 
for i in range(len(testYears)):
    year = testYears[i]
    month = testMonths[i]
    days = monthYear(year,month)
    if days == testResults[i]:
        print({'Year': year,'Month Number': month,'Number of Days': days})
    else:
        print('The process was unsuccessful.')