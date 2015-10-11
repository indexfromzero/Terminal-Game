class Item(object):

    # TO DO.. add a size variable to keep track how big item is
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        
    def description(self):
        print("    Name: ", self.name)
        print("    Description: ", self.desc)
