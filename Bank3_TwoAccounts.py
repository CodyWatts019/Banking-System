#Non-OOP
#Bank 3
#Two Accounts

from codecs import namereplace_errors


account0Name = ''
account0Balance = 0
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password = ''
nAccount = 0

def newAccount(accountNumber, name, balance, password):
    global account0Name,account0Balance,account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password

    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password

def shoe():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if account0Name != '':
        print('Account 0')
        print('     Name', account0Name)
        print('     Balance', account0Name)
        print('     Password', account0Password)
        print()

    if account1Name != '':
        print('Account 1')
        print('     Name', account1Name)
        print('     Balance', account1Balance)
        print('     Password', account1Password)
        print()

def getBalance(accountNumber, password):
    global account0Name,account0Balance,account0Password
    global account1Name,account1Balance,account1Password

    if accountNumber == 0:
        if password != account0Password:
            print('Incorrct Password.')
            return None
        return account0Balance

    if accountNumber == 1:
        if password != account1Password:
            print('Incorrect Password.')
            return None
        return account1Balance

def deposit(accountNumber, amountToDeposit, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if amountToDeposit < 0:
            print('You cannot deposit a negative amount!')
            return None

        if password != account0Password:
            print('Incorrect Password.')
            return None

        account0Balance = account0Balance + amountToDeposit
        return account0Balance

    if accountNumber == 1:
        if amountToDeposit < 0:
            print('You cannot deposit a negative balance!')
            return None

        if password != account1Password:
            print('Incorrect Password.')
            return None

        account1Balance = account1Balance + amountToDeposit
        return account1Balance

def withdrawl(accountNumber, amoutnToWithdraw, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if amoutnToWithdraw < 0:
            print('You cannot withdraw a negative amount.')
            return None

        if password != account0Password:
            print('Incorrect password for this account.')
            return None

        if amoutnToWithdraw > account0Balance:
            print('You cannot withdraw more than you have in your account.')
            return None

        account0Balance = account0Balance - amoutnToWithdraw

    if accountNumber == 1:
        if amoutnToWithdraw < 0:
            print('You cannot withdraw a negative amount.')
            return None

        if password != account1Password:
            print('Incorrect password for thid account.')
            return None

        if amoutnToWithdraw > account1Balance:
            print('You cannot withdrew nore than you have in your account.')

        account1Balance = account1Balance - amoutnToWithdraw

account0Name = 'Joe'
account1Name = "Eoj"
account0Balance = 100
account1Balance = 200
account0Password = 'soup'
account1Password = 'pous'

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposite')
    print('Press w to make a withdrawl')
    print('Press s to shoe the account')
    print('press q to quit')
    print()

    action = input('what do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get Balance: ')
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter the amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is: ', newBalance)

    elif action == 's':
        print('Show:')
        print('     Name', account0Name,account1Name)
        print('     Balance', account0Balance, account1Balance)
        print('     Password', account0Password, account1Password)
        print()

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw: ')

        userWithdrawalAmount = input('Please enter the amount to withdraw: ')
        userWithdrawalAmount = int(userWithdrawalAmount)
        userPassword = input('Please enter the password: ')

        if userWithdrawalAmount < 0:
            print('You vannot withdraw a negarive amount')

        elif userPassword != account0Password:
            print('Incorrect password for this account.')
        
        elif userPassword != account1Password:
            print('Incorrect password for thid account.')

        elif userWithdrawalAmount > account0Balance:
            print('You cannot withdraw more than you have in your account.')

        elif userWithdrawalAmount > account1Balance:
            print('You cannot withdraw more than you have in your account.')

        else:
            account0Balance = account0Balance - userWithdrawalAmount
            print('Your new balance is: ', account0Balance)

            account1Balance = account1Balance - userWithdrawalAmount
            print('Your new balance is: ', account1Balance)

print('Done')