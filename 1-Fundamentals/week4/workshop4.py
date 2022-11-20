    
class User:
    def __init__(self , name , pin , password):
        self.name = name
        self.password = password
        self.pin = pin
        #task 2
    def change_name(self,new_name):
        self.name = new_name
        
    def change_pin(self, new_pin):
        self.pin = new_pin 
        
    def change_password(self, new_password):
        self.password = new_password

user2 = User('Bill' , 1234 , "password")
print(user2.name , user2.pin , user2.password)

user2.change_name("Holt")
user2.change_pin(6589)
user2.change_password('rollword')
print(user2.name , user2.pin , user2.password)

class BankUser(User):                       #setting a default parameter value 
    def __init__(self, name, pin, password, balance = 0):
        super().__init__(name, pin, password)
        self.balance = balance
    def show_balance(self):     
        print(self.balance)       
    def withdraw(self,withdrawl_amt):
        self.balance -= withdrawl_amt       
    def deposit(self, deposit_amt):
        self.balance += deposit_amt

    #will work on and resubmit
   # def transfer_money(self):
        



user1 = BankUser("Jim", 1234, "password")
user1.show_balance()
user1.deposit(50)
user1.withdraw(25)
user1.show_balance()
user3 = BankUser("Ron" , 7568 , "returnf" )

user3.show_balance()














#driver code for task 1
# user1 = User('Bob' , 1234 , 'password')

#driver code for task2
#user2 = User('Bill' , 1234 , "password")
#print(user2.name , user2.pin , user2.password)

#user1 = BankUser("Jim", 1234, "password", balance = 0 )
#print( user1.name, user1.pin, user1.password, user1.balance)