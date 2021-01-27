from swap_meet.item import Item

class Electronics(Item):

    def __init__(self, condition = 0.0, age = 0):
        self.category = "Electronics"
        self.condition = condition
        self.age = age


    def __str__(self):
        return "A gadget full of buttons and secrets."

    def long_description(self):
        if self.condition > 4.0:
            return "Looks like it was just pulled out of the box for the first time!"
        else:
            return "Probably broken, but retro!"