# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:47:58 2022

@author: DTIC
"""

def añoBisiesto(año):
    if año>1582:
        if (año%4)==0 and (año%100)!=0 and (año%400)==0:
            return True
        else:
            return False
    else:
        return None
 
def diasMeses(año, mes):
    meses=[1,2,3,4,5,6,7,8,9,10,11,12]
    mesestre=[4,6,9,11]
    x=añoBisiesto(año)
    if mes in meses:
        if mes==2:
            if x:
                return 29 
            else:
                return 28
        elif mes in mesestre:
            return 30
        else:
            return 31
    else:
        return None
 
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 9]
testResults = [29, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = diasMeses(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")