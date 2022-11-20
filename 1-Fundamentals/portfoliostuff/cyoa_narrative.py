#opening scene

while True:
    print("Welcome to the Trail!")
    print("The forest smells of evergreen and rain, and the sun is shining through the branches.\nThere is a fork in the path. Do you pick a path, or do you go back the way you came?")

    option = input("1.) Take the left fork, looks like it goes higher up the mountain. \n2.) Take the middle fork, it looks like there's some path and a clearing ahead. \n3.)Take the right fork, looks like it goes down the mountain.\n4.Turn around and head back to the trailhead. It's way darker than you thought it would be.")
    if option == "1":
        print("You walk up the left fork, and hit a series of switchbacks. You hear rustling in the trees ahead of you. It looks like there is a break in the treeline \nWhat do you do now?")
        option_a = input("1.) Inspect the rustling in the trees\n2.)Walk past the trees and ignore the sound\n3.)Investigate the break in the treeline")
        if option_a == "1": #scare
            print("You locate the rustling bush and walk towards it. The rustling suddenly stops. A pair of eyes appears within the bush, and just as quickly dissapears.")
        elif option_a == "2": #death
            print("You walk past the trees, assuming it's the sound of an animal in the underbrush. As you pass the treeline, a loud rapid stomping sounds behind you. As you turn you feel something hit the side of your head, and your vision goes black. You hit the ground and all you remember is something hot and wet all over your face. \nYOU'RE DEAD")
        elif option_a == "3": #pursuit
            print("As you approach the treeline you see a blur of movement in the gap. You feal a rush of fear and turn on your heel")
            option_pursuit = input('What do you do?')
            print("1.) Run further up the trail \n2.) Run back down the trail")
            if input == '1': "You hear a dragging sound behind you."
                pass

    # elif option == "2":
    #     print("You choose the middle fork, and proceed along the trail. The light seems to dim rapidly as you proceed. You see the clearing and the light there is bright.")
    #     option_b = input("1.) Enter the clearing\n 2.)Turn back around and proceed back down the trail \n3.)Go around the clearing and inspect the surround trees")
    #     if option_b == "1": death
    #         print("As you enter the clearing, a low screech sounds from above. You start to look up but it's too late!. You register the blue sky and then see nothing.") 
    #     elif option_b == "2":
    #         print("")
    #     elif option_b == "3":
    #         print("")
    #     break
    # elif option == "3":
    #     print("You choose the right fork, and quickly realize this trail fork is rocky and uneven, with anklebreakers all over the trail. ")
    #     option_c = input("1.)Proceed down the trail.\n2.)Turn back around.\n3.)Go off the trail.")
    #     if option_c == "1":
    #         print("")
    #     elif option_c == "2":
    #         print("")
    #     elif option_c == "3":
    #         print("")
    #     break
    # else:
    #     print("Please pick 1, 2, or 3")


