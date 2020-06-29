#num = float(input('Decimal number between 0 and 1: '))
num = 0.333
p = 0
binary = '0.'
ans = 0

if num == 0:
    binary = ans
else:
    while ans!=1:
        ans = num*2
        if num*2 < 1:
            binary += '0'
        else:
            binary += '1'
            print(binary)
        num = (num*2)%1
        print(f'num = {num}')
    
print(binary)
