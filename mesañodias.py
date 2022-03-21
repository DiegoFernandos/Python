# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:38:30 2022

@author: DTIC
"""

def isYearLeap(year):


def daysInMonth(year, month):
 

testYears = [1900, 2000, 2016, 1987]

testMonths = [2, 2, 1, 11]

testResults = [28, 29, 31, 30]

for i in range(len(testYears)):

	yr = testYears[i]

	mo = testMonths[i]

	print(yr, mo, "->", end="")

	result = daysInMonth(yr, mo)

	if result == testResults[i]:

		print("OK")

	else:

		print("Error")