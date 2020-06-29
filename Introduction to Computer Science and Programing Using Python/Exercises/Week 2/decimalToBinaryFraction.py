.37# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:13:04 2016

@author: ericgrimson
"""

#x = float(input('Enter a decimal number between 0 and 1: '))
x = 0.333

p = 0
while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1
num = int(x*(2**p))
print(f'num1 = {num}')


result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
    print(result)

for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))
print('')
result= '0' +result
