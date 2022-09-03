#Non-OOP
#Bank 2
#Single account

accountName = ''
accountBalance = ''
accountPassword = ''

1

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password

def show():
    global accountName, accountBalance, accountPassword
    print('     Name', accountName)
    print('     Balance', accountBalance)
    print('     Password', accountPassword)
    print()

2

def deposit(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Incorrect Password')
        return None
    return accountBalance

3

def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('You can not deposite a negative amount!')
        return None

    if password != accountPassword:
        print('Incorrect Password')
        return None

    accountBalance = accountBalance + amountToDeposit
    return accountBalance

4
def withdraw (amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('You can not withdraw a negative amount.')
        return None

    if password != accountPassword:
        print('Incorrect password for thhs account.')
        return None

    if amountToWithdraw > accountBalance:
        print('You cannot withdraw more than you have in your accont.')
        return None

    accountBalance = accountBalance - amountToWithdraw
    return accountBalance

newAccount('Joe', 100, 'soup')

while True:
    print('Press b to get the balance')
    print('Press d to nake a deposit')
    print('Press w to nake a withdrawl')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get Balance: ')
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print('Your balance is: ', theBalance)

        elif action =='d':
            print('Deposit: ')
            userDepositAmount = input('Please enter amount to deposit: ')
            userDepositAmount = int(userDepositAmount)
            userPassword = input('Please enter the password: ')

            newBalance = deposit(userDepositAmount, userPassword)
            if newBalance is not None:
                print('Your new balance is: ', newBalance)

print('Done')