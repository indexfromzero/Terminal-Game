class Backpack(object):
    #global vars.. each pack will contain contents
    # contents will be a list of items
    contents = []
    empty = True
    level = 1
    empty_spaces = 10
    def __init__(self, items):
        # add all starting items to contents
        for item in items:
            self.contents.append(item)
    
        # check if pack is empty
        if not self.contents:
            empty = True
        else:
            empty = False

    def show_contents(self):
        print("Heres what you have: ")
        for item in self.contents:
            item.description()
        return
    
    def count_items(self):
        print("Items in Bag: ", len(self.contents))
        return len(self.contents)

    def is_full(self):
        if (self.empty_spaces - self.count_items()) > 0:
            print("Bag not full... you have %s empty spaces left" % self.empty_spaces)
            return False
        else:
            print("Bag full.. drop something to free up space")
            return True

    def add_item(self, item):
        self.contents.append(item)
        print("Item Added to Bag")
        print("Current contents")
        for item in self.contents:
            item.description()
        return
        
    def drop_item(self, item):
        if item in self.contents:
            self.contents.remove(item)
            return
        else:
            print("Item not in bag.. nothing removed")
            return
    
