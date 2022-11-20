


class Monster:
    def __init__(self, name, hp, attack , initiative):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.initiative = initiative
        # test access to values

monster1 = Monster("Golem", 60, 10, 2 )

monster2 = Monster("Serpent",25 , 20, 6)
# print(monster1.attack, monster1.defense, monster1.name)
 



class Player:
    def __init__(self, name, hp, attack, initiative):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.initiative = initiative
player1 = Player("James", 40 , 8, 5 )

player2 = Player("Margot", 45, 7, 5)
# print(player1.attack, player1.defense, player1.name)


def player1_initiative_test():
    while monster1.hp > 0:
        if player1.initiative > monster1.initiative:
            monster1.hp = monster1.hp - player1.attack
            print(monster1.name , "has" , monster1.hp , "health remaining!") 
            
        elif monster1.hp <= 0:
            print(monster1.name , "has been killed!")



def monster1_initiative_test():
    while player1.hp > 0:
        if monster1.initiative > player1.initiative:
            player1.hp = player1.hp - monster1.attack 
            print(player1.name , "has" , player1.hp , "health remaining!")
        elif monster1.initiative < player1.initiative:
            player1.hp = player1.hp - monster1.attack 
            print(player1.name , "has" , player1.hp , "health remaining!")
        elif player1.hp <= 0:
            print(player1.name , "has been killed!")