def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 1:
        return base
    else:
        return base * recurPower(base, exp-1)

print(recurPower(2,4))
