'''
Exercise 7.1.
Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt
that takes a as a parameter, chooses a reasonable value of x, and returns an
estimate of the square root of a.
To test it, write a function named test_square_root that prints a table like this:
a   mysqrt(a)      math.sqrt(a)   diff
-   ---------      ------------   ----
1.0 1.0            1.0            0.0
2.0 1.41421356237  1.41421356237  2.22044604925e-16
3.0 1.73205080757  1.73205080757  0.0
4.0 2.0            2.0            0.0
5.0 2.2360679775   2.2360679775   0.0
6.0 2.44948974278  2.44948974278  0.0
7.0 2.64575131106  2.64575131106  0.0
8.0 2.82842712475  2.82842712475  4.4408920985e-16
9.0 3.0            3.0            0.0
The first column is a number, a;
the second column is the square root of a computed with mysqrt;
the third column is the square root computed by math.sqrt;
the fourth column is the absolute value of the difference between the two estimates.
'''
from math import sqrt

def mysqrt(a):
    '''
    Calculates the square root of "a" using Newton's method.
    a: positive integer
    returns: a aproximation tu the square root of a
    '''
    x = a/2
    while True:
        square_root = (x + a/x) / 2
        if abs(square_root - x) < 0.0000000001:
            return square_root
        else:
            x = square_root
            
def test_square_root(test_list):
    '''
    Executes the function mysqrt with a predefine list of values
    test_list: lit containg multiple values for testing
    return: a table informing the value, the square_root calculated by mysqrt(), the square root and the difference bettween values
    '''    
    first_column = 'a'
    seccond_column = 'mysqrt(a)'
    third_column = 'math.sqrt(a)'
    fourth_column = 'diff'
    
    print(f'{first_column:<3} {seccond_column:<13} {third_column:<13} {fourth_column}')
    print('{:3} {:13} {:13} {:13}'.format('-'*1, '-'*9, '-'*12, '-'*4))
    
    for number in test_list:
        print(f'{number:<3.1f} {mysqrt(number):<11.11f} {sqrt(number):<13.11f} {abs(mysqrt(number)-sqrt(number)):.11f}')
test_square_root([1,2,3,4,5,6,7,8,9])