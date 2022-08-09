#Non-OOP
#Bank Version 1
#Single account

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print()
    print('Press b to get the BALANCE')
    print('Press d to make a DEPOSITE')
    print('Press w to make the WITHDRAWAL')
    print('Press s to show the ACCOUNT')
    print('Press q to QUIT')
    print()

    action = input('What do you want to do?')
    action = action.lower() #force lowercase
    action = action[0] #just use first letter
    print()

    if action == 'b':
        print('Get Balance:')
        userPassword = input ('Please enter the password; ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            print('Your balance is:', accountBalance)

    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input ('Please enter anount to deposit: ')
        userDepositAmount = int (userDepositAmount)
        userPassword = input ('Please enter the password: ')

        if userDepositAmount < 0:
            print('You can not deposite a negative amount!')
        elif userPassword != accountPassword:
            print('Incorrect password')
        else:
            accountBalance = accountBalance + userDepositAmount
            print('Your new balance is: ', accountBalance)

    elif action == 's':
        print('Show: ')
        print('     Name', accountName)
        print('     Balance:', accountBalance)
        print('     Paassword:', accountPassword)
        print()

    elif action == 'q':
        break

    elif action == 'w':
        print('Woithdraw: ')

        userWithdrawAmount = input('Please enter the amoint to withdraw: ')
        userWithdrawAmount = int (userWithdrawAmount)
        userPassword = input ('Please enter the password: ')

        if userWithdrawAmount < 0:
            print('You can not withdraw a negative amopunt.')
            
        elif userPassword != accountPassword:
            print('Incorrect password for this account.')

        elif userWithdrawAmount > accountBalance:
            print('You cannot withdraw more than yyou have un your account')

        else:
            accountBalance = accountBalance - userWithdrawAmount
            print('Your new balance is: ',  accountBalance)

print('Done')