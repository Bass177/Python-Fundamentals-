class User:
    def __init__(self , name, email, password) :
        self.name = name
        self.email = email
        self.password = password 


  
class BankUser(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0


    def check_balance(self):
        print(self.name, "has an account balance of:" , self.balance)

bankuser1 = BankUser("Jaxon" , "Jaxon@SOA.org" , "badboyron")


print(bankuser1.name , bankuser1.email)


class Phone:
    def __init__(self, brand , series , cost):
        self.brand = brand
        self.series = series
        self.cost = cost 