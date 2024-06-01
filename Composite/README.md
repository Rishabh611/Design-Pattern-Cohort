# Composite pattern
'''
1. what:
    - different from composition
    - 


2. why, when
    - when you have a tree like strucuture and all the node implement a particular interface
    - we want to calculate something(invoke a method) on the entire tree

3. strategy to implement

4. implementation
'''
'''
OO World
 - code reusability
 - extensibility

Code reusability:
    - inheritence
    - composition(have an object of another class in your class)

Inheritence:
class A:
    pass
classB(A):
    # now B can access properties of A

Composition:
class A:
    pass

classB:
    a = A() # now B has an object class A
'''

# Implementation:
from abc import ABC, abstractmethod

class Entity(ABC):
    @abstractmethod
    def calculate_price(self) -> int:
        pass

class Common:
    def __init__(self, name, price):
        self.name = name
        self.price = price

item = Item('apple', 50)
item.common.name
class Item(Entity, Common):
    def __init__(self, name, price):
        common = Common(name, price)
        Common.__init__(name, price)
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

class A:
    some data
    some methods to work on that data


