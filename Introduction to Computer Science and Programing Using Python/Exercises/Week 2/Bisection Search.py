x = 23
epsilon = 0.001
guess = x/2
tries = 0

while abs(guess**2- x) >= epsilon:
    if guess**2 > x:
        guess /=2
    else:
        guess *=1.5
    tries +=1

print(f'Number of tries: {tries}')
print(f'Guess = {guess}')
