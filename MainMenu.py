from Player import Player
from Backpack import Backpack
from Item import Item
import time

class MainMenu(object):

    character_choice = 'None'

    def __init__(self):
        self.opening_message()
        
    def line_break(self):
        print("-------------------------------")
        return

    def opening_message(self):
        print("So you think you can complete the adventure...")
        time.sleep(1)
        self.choose_character()

    def choose_character(self):
        # This function will take input from user as they choose there character
        chars = {1: 'Warrior', 2: 'Wizard', 3: 'Sneak', 4: 'Nerd'}
        player = 'None'
        self.show_character_choices()
        chosen = False
        while chosen == False:
            choice = input("Enter the corresponding number to the char u want: ")
            print(choice)
            if choice == '1':
                player = chars[1]
                chosen = True
            elif choice == '2':
                player = chars[2]
                chosen = True
            elif choice == '3':
                player = chars[3]
                chosen = True
            elif choice == '4':
                player = chars[4]
                chosen = True
            else:
                print("Invalid Choice... choose again")

        self.line_break()
        print("You have chosen: %s" % player)
        print("Good Luck...")
        # TO DO.. Add shit here other options or whatever.. intro story
        
        self.line_break()
        
    def show_character_choices(self):
        # After the classes are developed, this will show the choices
        # along with the pros & cons of each
        # as of now its just chars I wrote in
        self.line_break()
        print("Character Classes: ")
        print("1 ... Warrior")
        print("2 ... Wizard")
        print("3 ... Sneak")
        print("4 ... Nerd")
        self.line_break()
        return
        
if __name__ == "__main__":
    start = MainMenu()
    
