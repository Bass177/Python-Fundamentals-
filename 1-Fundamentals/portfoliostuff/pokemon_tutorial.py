import time 
import numpy as np 
import sys 

# delay printing 
def delay_print(s):
    #print 0ne character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

#create a class
class Monster:
    def __init__(self, name, attack, defense, speed, health = '==========' )
        #save variables as attributes
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.health = health

    def monster_fight(self, Player):
        #allows monster to fight player

        #print battle information

        print("-----DANGER-----")
        print(f"\n{self.name}"):
        print(self.attack,self.defense, self.health)

        time.sleep(2)

    while (self.bars > 0) and (Player.bars > 0):
        #print health of each entity 
        print(f"{self.name}\t\tHLTH\t{self.health}")
        print(f"{Player.name}\t\tHLTH\t{Player.health}")    
        


class Player:
    def __init__(self, name, attack, defense, speed, health = '==========' )
        #save variables as attributes
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.health = health

    def player_fight(self, Monster):
        #allows monster to fight player

        #print battle information

        print("-----DANGER-----")
        print(f"\n{self.name}")
        print(self.attack,self.defense, self.health)

        time.sleep(2)
    # continue the fight while health remain???
    while (self.bars > 0) and (Monster.bars > 0):
        #print health of each entity 
        print(f"{self.name}\t\tHLTH\t{self.health}")
        print(f"{Monster.name}\t\tHLTH\t{Monster.health}")    

        print(f'Help me, theres a {Monster.name}! HELP!')
        for i, x in enumerate(self.moves):
            print(f"{i+1}.", x)    
        index = int(input("Pick a move:"))
        delay_print(f"{self.name} used {moves[index-1]}!")
        time.sleep(1)

        #determine damage

        Monster.bars -= self.attack


if __name__ == '__main__':
    pass

