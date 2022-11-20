import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    input("Press ENTER to pick a card or Q and Enter to quit")
    if input() == "":

        card = random.choice(diamonds)
        print("You drew" , card )
        diamonds.remove(card)

        hand.append(card)
        print("Deck :" , diamonds)
        print( "Hand :" , hand)
    elif input() == "Q" :
        break

    else :
        print("Invalid Input! Please press enter or Q to exit the game.")


print("All out of cards, thanks for playing!")




