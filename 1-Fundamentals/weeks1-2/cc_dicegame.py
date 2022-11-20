import random

high_score = 0


def dice_game():
    while True:
        global high_score
        print("Current High Score:" + str(high_score))
        print(("1) Roll Dice \n2) Exit Game")) 
choice = input("Enter your choice (1 or 2?)")

if choice == "1" :
    die_one = random.randint(1, 6)
    die_two = random.randint(1, 6)
    die_total = die_one + die_two
    print("You rolled a " , str(die_one) , "and a" ,  str(die_two) , "for a total of" , str(die_total))

    if die_total > high_score :
        print("New High Score!")

    elif choice == "2" :
        print("Come Again!")

         
    
    else: 
        print("Please choose 1 or 2")

dice_game()
