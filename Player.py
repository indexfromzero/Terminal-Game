class Player(object):
    # global vars.. all players start with the same
    health = 100
    exp = 0
    level = 1
    # constructor
    def __init__(self, name, attack, defense, luck, backpack):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.luck = luck
        self.backpack = backpack
    # print picture of player aka stats and gear n shit
    def show_player_stats(self):
        print("----------------------------------")
        print("Name:    ", self.name)
        print("Health:  ", self.health)
        print("Level:   ", self.level)
        print("EXP:     ", self.exp)
        print("Attack:  ", self.attack)
        print("Defense: ", self.defense)
        print("Luck:    ", self.luck)
        print("----------------------------------")
    # show whats in the player's backpack
    def show_backpack(self):
        print("----------------------------------")
        print("Backpack Contents: ")
        i = 1
        for item in self.backpack.contents:
            print("Item: ", i)
            item.description()
            i = i + 1
        print("----------------------------------")
