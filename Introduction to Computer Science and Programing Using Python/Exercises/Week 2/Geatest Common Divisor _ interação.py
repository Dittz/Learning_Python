def gcd(a,b):
    if a < b:
        divisor = a
        while True:
            if a == 1:
                return a
            elif a % divisor == 0 and b% divisor == 0:
                return divisor
            else:
                divisor -=1
                
                    
    if a > b:
        divisor = b
        while True:
            if a == 1:
                return a
            elif a % divisor == 0 and b% divisor == 0:
                return divisor
            else:
                divisor -=1
