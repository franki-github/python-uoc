
from abc import ABC, abstractmethod
from products.food_package import FoodPackage, Wrapping, Bottle, Glass, Box

#clase abstracta donde el resto de clases heredaran los metodos y atributos
class Product(ABC):
    def __init__(self,id:str,name:str,price:float):
      self.id = id
      self.name = name
      self.price = price     
    
    def describe(self):
        return f"Product - Type: {self.type()}, Name: {self.name}, Id: {self.id} , Price: {self.price} , {self.foodPackage().describe()}."   
    
    @abstractmethod
    def type(self) -> str:
        pass
    @abstractmethod
    def foodPackage(self)->FoodPackage:        
        pass
    

class Hamburger(Product):
    #  constructor de la clase, donde inicializamos atributos de la clase padre 
    # usando super()
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburguesa"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
class Soda(Product):
    #Write your code 
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price) 
    def type(self) -> str:
        return "Soda"
    def foodPackage(self) -> FoodPackage:
        return Bottle()
    pass

class Drink(Product):
    #Write your code here
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Drink"
    def foodPackage(self) -> FoodPackage:
        return Glass()
    pass

class HappyMeal(Product):
    #Write your code here
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Happy Meal"
    def foodPackage(self) -> FoodPackage:
        return Box()
    pass