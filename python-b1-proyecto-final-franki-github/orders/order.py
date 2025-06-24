
from users import *
from products import *

#clase Order, guarda la comanda de un cliente
#contiene el cajero que ha atendido al cliente y la lista de productos
class Order:
  def __init__(self, cashier:Cashier, customer:Customer): 
    self.cashier = cashier
    self.customer = customer
    self.products = []

  
  def add(self, product):
        #Write your code here

    #agregamos el producto a la lista de productos
    self.products.append(product)
    #imprimimos el producto agregado
    print(f"Producto {product.name} añadido a la comanda.")

    #imprimimos la lista de productos
    print("Productos de la comanda:")
    for product in self.products:
          print(product.describe())
    #imprimimos el total de la orden
    print(f"Total importe: {self.calculateTotal()}")
     
    pass

  def calculateTotal(self) -> float:
    #Write your code here
    #inicializamos el total a 0
    total = 0
    #recorremos la lista de productos
    for product in self.products:
      #sumamos el precio de cada producto al total
      total += product.price
    #devolvemos el total
    return total
    #imprimimos el total
    print(f"Total importe: {total}")
    
    pass
  
  
   # mostramos la orden , un saludo + quien ha atendido + produtos + total importe de la orden
   #Write your code here

  def show(self):    
    print("Hola : "+self.customer.describe())
    print("Te ha atendido el cajero : "+self.cashier.describe())
    for product in self.products:
      print(product.describe())
    print(f"Total importe : {self.calculateTotal()}")
