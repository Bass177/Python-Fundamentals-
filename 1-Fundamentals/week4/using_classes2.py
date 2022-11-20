class User:
    def __init__(self , name, email, password) :
        self.name = name
        self.email = email
        self.password = password 


    def change_password(self, password) :
        self.password = password
        print('Your password has been changed to' , self.password)

user1 = User("John" , "john@john.com" , "johnspassword")
print("My name is " , user1.name,"my email is" , user1.email, "and my password is" ,user1.password ) 
user1.change_password("bestpassword")
print(user1.password)