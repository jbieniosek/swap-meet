class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.category == category:
                result.append(item)
        return result
    
    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        best_item = None
        for item in items:
            if best_item == None:
                best_item = item
            if item.condition > best_item.condition:
                best_item = item
        return best_item
    
    def swap_first_item(self, swap_vendor):
        if len(swap_vendor.inventory) < 1 or len(self.inventory) < 1:
            return False
        first_item = self.inventory[0]
        self.inventory[0] = swap_vendor.inventory[0]
        swap_vendor.inventory[0] = first_item
        return True
    
    def get_newest(self):
        newest = None
        for item in self.inventory:
            if newest == None:
                newest = item
            if item.age < newest.age:
                newest = item
        return newest

    def swap_by_newest(self, swap_vendor):
        my_best = self.get_newest()
        their_best = swap_vendor.get_newest()
        if not my_best or not their_best:
            return False
        self.inventory.remove(my_best)
        self.inventory.append(their_best)
        other.inventory.remove(their_best)
        other.inventory.append(my_best)
        return True


    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if not my_best or not their_best:
            return False
        self.inventory.remove(my_best)
        self.inventory.append(their_best)
        other.inventory.remove(their_best)
        other.inventory.append(my_best)
        return True
