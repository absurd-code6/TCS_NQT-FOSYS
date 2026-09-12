class Car:
    def __init__(self,brand,price):
        self.__price=price
        self.__brand=brand
        #What does __price (double underscore) mean?

#When you write:

#self.__price = price

#the double underscore (__) triggers something called name mangling.

# What is name mangling?

#Python internally changes the variable name to make it harder to access 
# directly from outside the class.

#So:

#self.__price

#becomes:

#self._Car__price

#This is done to:

#Avoid accidental modification
#Prevent name conflicts in subclasses
#Encourage use of getters/setters
       
        
    def getBrand(self):
        return self.__brand
    def setBrand(self,brand):
        self.__brand=brand
    
    def getPrice(self):
        return self.__price
    def setPrice(self,price):
        self.__price=price
    def display(self):
        print("Price",self.__price)
        print("Brand",self.__brand)
        
#Creating object using constructor
car1 = Car("Toyota", 20000)
car1.display()
# Accessing using getters
# Modifing using setters
car1.setBrand("Mercedes")
car1.setPrice(1200000)
print("\nAfter modification\n")
print("Brand:", car1.getBrand())
print("Price:", car1.getPrice())

'''. self.price (no underscore)
self.price = price
✅ Public variable
Can be accessed and modified from anywhere
No restrictions at all

Example:

car.price = 30000   # Works fine
print(car.price)    # Works fine

👉 Use this when you don’t need control or protection

🔹 2. self._price (single underscore)
self._price = price
⚠️ “Protected” (by convention only)
Still accessible from outside
Signals: “this is internal, don’t touch directly”

Example:

car._price = 30000   # Works, but not recommended

👉 This is just a warning to programmers, not enforced by Python

🔹 3. self.__price (double underscore)
self.__price = price
🔐 Private (name mangling happens)

Python internally renames it to:

_Car__price
Cannot be accessed directly like car.__price

Example:

print(car.__price)       # ❌ Error
print(car._Car__price)   # ✅ Works (but should not be used)

👉 Used when you want stronger protection and controlled access

⚠️ Why self.price and self.__price are different
self.price = 20000
self.__price = 30000

These are stored separately as:

price
_Car__price

So they are completely different variables, not related.'''

'''Simple takeaway
__variable = private (mangled name)
Use it when you want to control access via methods
It's not truly hidden, just protected by convention + renaming'''
