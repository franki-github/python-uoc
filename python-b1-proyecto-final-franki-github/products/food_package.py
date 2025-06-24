

#Write your code 
from abc import ABC, abstractmethod

#clase abstracta donde el resto de clases heredaran los metodos y atributos
class FoodPackage (ABC): 
    @abstractmethod
    def pack(self)  -> str:
        pass
    @abstractmethod
    def material(self) -> str:
        pass
    def describe(self):
        return f"Empaque: {self.pack()} , Material: {self.material()}"    
    

#definmos las clases que heredan de la clase abstracta FoodPackage
#cada clase retornara el tipo de empaque y el material que hayamos predefinido
class Wrapping(FoodPackage):  
  #Write your code
    def pack(self): 
       return "Food Wrap Paper" 
    def material(self): 
       return "Aluminium" 
  
    pass

class Bottle(FoodPackage):  
  #Write your code 
    def pack(self): 
       return "Botella" 
    def material(self): 
       return "Carton"
    pass
      
class Glass(FoodPackage):  
  #Write your code here
    def pack(self): 
        return "Vaso" 
    def material(self): 
        return "Cristal"
  
    pass

class Box(FoodPackage):  
  #Write your code 
    def pack(self): 
        return "Box" 
    def material(self): 
        return "Papel duro"
  
    pass