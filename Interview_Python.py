def numbers(*args):
    '''*args is used in functions to pass a variable number of positional 
    arguments which is stored in the object in the form of tuple.'''

    for i in args:
        print(i)
        
numbers(1,235,6,7,90,101,22)
print(numbers.__doc__)

def docStr():
    '''A function's docstring must be the first statement inside the function.
These documentation strings are saved as a part of the metadata of the object
So python can access and display these doctrsings.These feaatures distinguish
docstrings from regular comments written using hash or triple quotes.'''
help(docStr)

#Variable Resolution(LEGB Rule)
x=440 #Global and not Built-In
def legb():
    x=7 #Enclosing
    def inner():
        x=420 #Local
        print(x)

    inner()
legb()

def dick(**kwargs):
    for i,j in kwargs.items():
         print(i,j)
    print(kwargs)

dick(name="John", age=20, course="Python")

