print('Please think of a number between 0 and 100! ')
high = 100
low = 0
ans = int((high+low)/2)

while True:
    print('Is your secret number {}? '.format(ans))
    user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if user == 'l':
        low = ans
        ans = int((high + low)/2.0)
    elif user == 'h':
        high = ans
        ans = int((high + low)/2.0)
    elif user == 'c':
        print('Game over. Your secret number was {}'.format(ans))
        break
