"""
Enunciado :
Crea una clase llamada "SafeWalletCredentials" que represente una
billetera electrónica que almacena monedas digitales y permite
establecer y obtener la contraseña de la billetera usando
encapsulamiento.

El constructor debe tener el parámetro password.

Parámetros:
    - password: una cadena que representa la contraseña de la
    billetera electrónica.

Métodos:
    - set_password(password): establece la contraseña de la billetera.
    - get_password(): devuelve la contraseña de la billetera.

Ejemplo:
    Entrada:
        safe_wallet = SafeWalletCredentials("1234")
        print(safe_wallet.get_password())
        safe_wallet.set_password("5678")
        print(safe_wallet.get_password())

    Salida:
        1234
        5678

Enunciat:
Crea una classe anomenada "SafeWalletCredentials" que representi una
cartera electrònica que emmagatzema monedes digitals i permet
establir i obtenir la contrasenya de la cartera usant
encapsulamiento.

El constructor ha de tenir el paràmetre password.

Paràmetres:
    - password: una cadena que representa la contrasenya de la
    cartera electrònica.

Mètodes:
    - set_password(password): estableix la contrasenya de la cartera.
    - get_password(): retorna la contrasenya de la cartera.

Exemple:
    Entrada:
        safe_wallet = SafeWalletCredentials("1234")
        print(safe_wallet.get_password())
        safe_wallet.set_password("5678")
        print(safe_wallet.get_password())

    Sortida:
        1234
        5678
"""

# Corret and overwrite class SafeWalletCredentials here
# el encapsulamiento oculta los datos y solo puedes acceder a traves de los metodos
# para acceder a los atributos privados se utiliza el guion bajo
# el guion bajo indica que el atributo es privado y no se puede acceder directamente
# 
class SafeWalletCredentials:
    def __init__(self, password):
        self.__password = password
        # Inicializa el atributo password
    def set_password(self, password):
        # Establece la contraseña de la billetera
        self.__password = password
    def get_password(self):
        # Devuelve la contraseña de la billetera
        return self.__password  
        
    pass


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# pedro_wallet = SafeWalletCredentials("1234A")
# print(pedro_wallet.get_password())
# pedro_wallet.set_password("A1B2c3")
# print(pedro_wallet.get_password())
