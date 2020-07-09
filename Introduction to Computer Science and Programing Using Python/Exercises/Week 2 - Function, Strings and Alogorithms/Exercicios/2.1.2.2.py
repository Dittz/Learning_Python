x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon: #confirms if guess^2 - x bigger or equal to 0.01
    if guess <= x: # if it is bigger increments the value of guess
        guess += step
    else:
        break   #if guess^2 - x is smaller than epsilon breaks the script

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
