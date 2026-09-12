#Write a program to add two objects using binary plus (+) operator overloading
class Add_num:
    def __init__(self,num):
        self.num=num
    def __add__(self,other):
        return self.num + other.num
print("Enter 2 numbers for addition:")
n1=int(input())
n2=int(input())
obj1=Add_num(n1)
obj2=Add_num(n2)
print(obj1+obj2)

    