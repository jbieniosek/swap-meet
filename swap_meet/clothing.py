from swap_meet.item import Item

class Clothing(Item):

    def __init__(self, condition = 0.0, age = 0):
        self.category = "Clothing"
        self.condition = condition
        self.age = age

    def __str__(self):
        return "The finest clothing you could wear."

    def long_description(self):
        if self.condition > 1.0:
            return "Clothing is clothing"
        else:
            return "Worn out, possibly fashionable, possibly extreme"