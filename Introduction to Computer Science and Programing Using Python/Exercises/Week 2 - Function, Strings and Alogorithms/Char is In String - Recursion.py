def isIn(char, aStr):
    pos = (0 + (len(aStr)))//2
    print(f'pos = {pos}')
    print(f'len(aStr) = {len(aStr)}')
    print(f'aStr = {aStr}')
    if len(aStr) == 1 and char != aStr:
        return False
    elif len(aStr) == 0:
        return False
    elif char == aStr[pos]:
        return True
    elif char > aStr[pos]:
        return isIn(char, aStr[pos:])
    elif char < aStr[pos]:
        return isIn(char, aStr[:pos])

    
