from Player import Player
from Item import Item
from Backpack import Backpack

# This will be the main method
if __name__ == "__main__":
    # create test items
    knife = Item("Rusty Knife", "an old dull thing")
    cup = Item("Wooden Cup", "an old cup to hold liquids")
    potion = Item("Useless Potion", "a useless potion that does nothing")

    # create test backpack
    bag = Backpack([knife, cup, potion])

    # create test player
    joe = Player("Joe", 10, 10, 5, bag)
    joe.show_player_stats()
    joe.show_backpack()
