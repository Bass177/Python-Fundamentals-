def show_homepage() :
    print("        === Donate Homepage ===         ")
    print(" -----------------------------------------")
    print("|   1.   Login    |   2.   Register       |")
    print(" ----------------------------------------- ")
    print("|   3.   Donate   |   4.   Show Donations |")
    print(" -----------------------------------------")
    print("|               5.  Exit                  |")
    print(" -----------------------------------------")

    
def donate(username):
    donation_amt = (input("Enter amount to donate"))

    donation = donation_amt 
    print("Thank you for donating" , username)
    return donation  

def show_donations( donations):
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently, there are no donations. =(")
    else:
        for donation in donations:
            print(str(donation)),