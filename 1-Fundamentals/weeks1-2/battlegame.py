wizard = "Wizard"
elf = "Elf"
human = "Human"
knight = "Knight"

hp_wizard = 70
hp_elf = 100
hp_human = 150
hp_knight = 220

wizard_damage = 150
elf_damage = 100
human_damage = 20
knight_damage = 60

dragon_hp = 300
dragon_damage = 50

#task 2

while True:

    print("Please choose a character\n 1. Wizard \n 2. Elf \n 3. Human \n 4. Knight")
    character = input("Choose your character!").lower().title()

    if character == "1" or character == "Wizard" : 
        character = wizard
        my_hp = hp_wizard
        my_damage = wizard_damage
        break
    if character == "2" or character == "Elf":
        character = elf
        my_hp = hp_elf
        my_damage = elf_damage
        break
    if character == "3" or character == "Human":
        character = human
        my_hp = hp_human
        my_damage = human_damage
        break
    if character == "4" or character == "Knight":
        character = knight
        my_hp = hp_knight
        my_damage = knight_damage

        break
    print("Unknown Character")

print("You have chosen: the " + character)
print("Health: " + str(my_hp))
print("Damage: " + str(my_damage))
#character attack
while True:
    dragon_hp = dragon_hp - my_damage
    print("The " + character, "damaged the Dragon!")
    print("")
    print("The Dragon has " + str(dragon_hp) + " health left.") 
    if dragon_hp <= 0 :
        print("The Dragon has lost the battle!")
        break
#dragon attack
    my_hp = my_hp - dragon_damage
    print("The Dragon dealt " + str(dragon_damage) + " damage to the " + character)
    print("")
    print("The " + character + " has " + str(my_hp) + " health left.")
    if my_hp <= 0:
        print("The " + character + " has lost the battle!")
        break