
from banking_pkg.account import deposit , withdraw , show_balance , logout

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

name = input("Please enter name to register.")

pin = input("Enter PIN")

balance = 0

print( name , "has been registered with a starting balance of $" , str(balance) , "dollars.")


while True :
    name_to_validate = input("Username Please!") 
    pin_to_validate = input("PIN Please!")

    if name_to_validate == name and pin_to_validate == pin : 
        print("Login Succesful!")
        break 

    else :
        print("Invalid Credentials")

while True : 
    atm_menu(name) 

    option = input("Choose an option:")
    if option == "1" :
        show_balance(balance) 

    elif option == "2" :
        balance = deposit(balance) 


    elif option == "3" :
        balance = withdraw(balance)

    elif option == "4" : 
        logout(name)
        break 

    else :
        print("Invalid credentials!")
        