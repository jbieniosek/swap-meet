class Item:
    def __init__(self, category = "", condition=0.0, age=0):
        self.category = category
        self.condition = condition
        self.age = age
    
    def __str__(self):
        return "Hello World!"

    def long_description(self):
        return "A Very Hello to the World!"