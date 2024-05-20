'''
3 sections:
1. creational patterns - create objects
2. strcutural patterns - prefer composition over inheritence (aggregation), to avoid problems like multiple inheritance, diamond prob etc..
3. behavioural patterns - how diff objects communicate with each other. 
'''
# Factory Design Pattern
- what it is
    - it creates objects depending on the param values
    - factory knows how to create objects so that the code doesn't have worry about those things.
- why, when
    - when the object creation is a painfully heavy process, may need to call APIs, DB queries to get data for object creation.
- strategy to implement
    - There is a factory class, which takes the params and the object class name to create and return the object to the caller
- implementation
'''
class Factory:
    def get_object(self, params: List[str], object_class_name: str):
        # get all data for object instantiation
        # create the object
        # return the object to the caller

class A:
    pass

class B:
    pass

caller_function():
    factory = Factory()
    a = factory.get_object(params, 'A')
'''

'''
class Factory:
    pass

class Component(ABC):
    @abstractmethod
    def create():
        pass

class ConcreteComponent1(Component):
    def create():
        product1 = ConcreteProduct1()
        print('creating product1')
        return product1

class Product(ABC):
    @abstractmethod
    def shape():
        pass

class ConcreteProduct1(Product):
    def shape():
        print('circular')

def caller():
    factory = Factory()
    component1 = ConcreteComponent1()
    #factory.register(component1)
    product = factory(component1).get_product()
'''

abstract factory = factory of factory