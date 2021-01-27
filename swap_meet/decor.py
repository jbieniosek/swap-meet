from swap_meet.item import Item

class Decor(Item):

    def __init__(self, condition = 0.0, age = 0):
        self.category = "Decor"
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Something to decorate your space."
    
    def long_description(self):
        if self.condition > 4.0:
            return "Very good condition"
        elif self.condition > 3.0 and self.condition <= 4.0:
            return "Pretty good condtion"
        elif self.condition > 2.0 and self.condition <= 3.0:
            return "Noticeable wear and tear"
        else:
            return "Fashionably rustic"