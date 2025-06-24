"""
El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ 
que tiene un constructor por defecto para los siguientes datos
'def  init (self, dni:str, name:str, age:int) ', 
con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones
 concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, 
 estas deben implementar los métodos anteriores y devolver un valor. 
 Adicionalmente, estas clases se diferencian por los parámetros 
 que reciben sus constructores, por tanto, debemos hacer uso de 
 herencia para inicializar el constructor de la clase padre 
 y agregar características propias a cada clase.

Keyword arguments:
argument -- description
Return: return_description
"""

from abc import ABC, abstractmethod

class User(ABC):
  def __init__(self,dni:str,name:str,age:int):
    self.dni = dni
    self.name = name
    self.age = age    
   
  @abstractmethod
  def describe(self):
      pass

class Cashier(User): 
  def __init__(self,dni:str,name:str,age:int,timetable:str,salary:float):
    #Write your code
    super().__init__(dni,name,age)
    self.timetable = timetable
    self.salary = salary  
    pass      
 
  def describe(self):
        return f"Cashier - Name: {self.name}, DNI: {self.dni} , Timetable: {self.timetable}, Salary: {self.salary}."
  

class Customer(User):
  def __init__(self,dni:str,name:str,age:int,email:str,postalcode:str):
    #Write your code here

    #heredamos de la clase User
    #inicializamos el constructor de la clase padre
    super().__init__(dni,name,age)
    #agregamos los atributos propios de la clase Customer
    #inicializamos los atributos propios de la clase Customer
    self.email = email
    self.postalcode = postalcode
       
    pass


  def describe(self):
        return f"Customer - Name: {self.name}, DNI: {self.dni} , Age: {self.age}, Email: {self.email}, Postal Code: {self.postalcode}"