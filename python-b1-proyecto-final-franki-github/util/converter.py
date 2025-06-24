
from abc import ABC, abstractmethod
import pandas as pd
from users import Customer
from users import Cashier
from products.product import Drink, Soda, Hamburger, HappyMeal

# Clase base abstracta de la cual heredan el resto de clases
class Converter(ABC):
    @abstractmethod
    def convert(self, dataFrame, *args) -> list:
        pass

    def print(self, obj_list):
        for obj in obj_list:
            print(obj)


# Convertidor de clientes
class CustomerConverter(Converter):
    def convert(self, dataFrame, *args):
        customers = []
        for _, row in dataFrame.iterrows():
            customer = Customer(
                name=row['name'],
                dni=row['dni'],
                age=row['age'],
                email=row['email'],
                postalcode=row['postalcode']
            )
            customers.append(customer)
        return customers


# Convertidor de cajeros

class CashierConverter(Converter):
    def convert(self, dataFrame, *args):
        cashiers = []
        for _, row in dataFrame.iterrows():
            cashier = Cashier(
                name=row['name'],
                dni=row['dni'],
                age=row['age'],
                timetable=row['timetable'],
                salary=row['salary']
            )
            cashiers.append(cashier)
        return cashiers


# Convertidor de productos

class ProductConverter(Converter):
    def convert(self, dataFrame, product_type, *args):
        products = []
        for _, row in dataFrame.iterrows():
            if product_type == 'drink':
                products.append(Drink(row['id'], row['name'], row['price']))
            elif product_type == 'soda':
                products.append(Soda(row['id'], row['name'], row['price']))
            elif product_type == 'hamburger':
                products.append(Hamburger(row['id'], row['name'], row['price']))
            elif product_type == 'happyMeal':
                products.append(HappyMeal(row['id'], row['name'], row['price']))
        return products
