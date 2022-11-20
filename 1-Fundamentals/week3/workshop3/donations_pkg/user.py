def login(database , username , password) :
    if username in database.keys() and database[username]== password:
        print("Welcome")
        return username

       
    elif username in database.keys() and database[username] != password:
        print("Wrong password!")
        return ""
    else :
        print("Failed Login")
        return ""
    
def register(database , username) :
    if username in database.keys() :
        print("Username already registered")
        return ""

    else :
        print("Username successfully registered")
        return username