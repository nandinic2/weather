import random

attack = random.randint(0,100)

class Pokemon():

    def __init__(self, hp, atk, name):
        self.hp = hp
        self.atk = atk
        self.name = name

    def battle(self,other):
        print(self.name, 'and', other.name, 'are fighting')
        other.hp = other.hp - self.atk
        print(other.name, 'now has', other.hp)
        # end condition
        if other.hp > 0:
            return other.battle(self)
        else:
            print(other.name, 'is knocked out')

# pokemon object
izzy = Pokemon(100, attack, 'izzy')
nick = Pokemon(100, attack, 'nick')
izzy.battle(nick)
