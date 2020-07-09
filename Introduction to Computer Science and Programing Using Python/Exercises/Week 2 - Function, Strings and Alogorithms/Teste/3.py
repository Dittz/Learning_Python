balance = 999999
annualInterestRate = 0.18
mr = annualInterestRate/12
newbalance = balance
low = balance/12
high = balance *((1+mr)**12)/12
payment = round((low +high)/2,2)
#print(f'1st low = {low}')
#print(f'1st high = {high}')
#print(f'1st payment = {payment}')


while True:
    newbalance = balance
    for i in range(12):
        newbalance = newbalance - payment
        newbalance = newbalance + (newbalance * mr)
    #print(f'new balance = {newbalance}')

    if newbalance >= 0.01:
        low = payment
        #print(f'low = {payment}')
        payment = (low + high) / 2
        #print(f'payment = {payment}')
    elif newbalance <= 0.009:
        high = payment
        #print(f'high = {payment}')
        payment = (low + high) / 2
        #print(f'payment = {payment}')
    else:
        payment = round(payment,2)
        print('Lowest Payment: ', payment)
        break
        
