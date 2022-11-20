def show_balance(balance) :
    print(balance)

def deposit(balance) :
    amount = input('Enter an amount to deposit:')
    print(amount) 
    return balance + float(amount)

def withdraw(balance) :
    amount = input("Enter an amount to withdraw:")
    return balance - float(amount)

def logout(name) :
    print("Goodbye" + name )

    