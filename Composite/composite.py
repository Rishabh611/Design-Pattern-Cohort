from abc import ABC, abstractmethod

class Entity(ABC):
    @abstractmethod
    def calculate_price(self) -> int:
        pass

class Item(Entity):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def calculate_price(self) -> int:
        return self.price

class Box(Entity):
    def __init__(self, name, items: list[Entity], price):
        self.name = name
        self.items = items
        self.price = price
    def calculate_price(self) -> int:
        total = 0
        for item in self.items:
            total += item.calculate_price()
        return total + self.price

burger = Item('burger', 100)
pizza = Item('pizza', 200)
chicken_wings = Item('chicken wings', 300)
pizza_box = Box('pizza_box', [pizza], 10)
burger_chicken_wings_box = Box('burger_chicken_wings_box', [burger, chicken_wings], 25)
final_package = Box('final_delivery', [pizza_box, burger_chicken_wings_box], 5)

print(final_package.calculate_price())
