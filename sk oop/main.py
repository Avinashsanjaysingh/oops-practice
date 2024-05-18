# class & object in python

# class is a blueprint for creating objects.

#creating claass

# class Student:
#     name = "Avinash singh"

#creating object (instance)

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)


# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)


# Constructor
# __init__ function

# All classses have a function called __init()__, which is always executed when the object is being initiated.

# creating class

class Student:

    # default constructors
    def __init__(self):
        pass

    college_name = "SMS college"    #class attribute

    # parameterized constructors
    def __init__(abcd, fullname):
        # print(abcd)
        abcd.name = fullname    # abcd is self & The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        print("Adding new student in Database.")

s1 = Student("Avinash")
print(s1.name)  #Avinash

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

s2 = Student("Arjun")
print(s2.name)
print(s2.college_name)
print()

# The data that is stored inside the variable, class & objects are known as "Attributes".


# Class & Instance Attributes

# Class.attr -> common for each objects
# obj.attr


# Methods -> Methods are functions that belongs to objects.

# creating class
class Student:
    def __init__(self, name, marks=30):
        self.name = name
        self.marks = marks

    # methods
    def hello(self):
        print("hello",self.name)

    def welcome(self):
        print(f"Welcome student, {self.name}")

    def get_marks(self):
        return self.marks

#creating object
s1 = Student("karan")
s1.hello()
s1.welcome()
print(s1.get_marks())
print()


# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Exams:
        
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    
    def marks_average(self):
        return (( self .sub1+ self .sub2+ self .sub3)/3)

details = Exams("Avinash", 56,88,96)
print(f"{details.name}'s average marks is {details.marks_average()}")
print()

class Student:
    def __init__(self, name, marks) :
        self.name = name
        self.marks = marks
    
    def get_avg (self) :
        sum = 0
        for val in self.marks:
            sum += val
        print (f"hi {self.name} your avg score is: {sum/3}")

s1 = Student("tony stark", [99, 98, 97])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()


# Static Methods -> Methods that don't use the self parameter (work at class level)

class Student:
    @staticmethod   #decorator
    def college():
        print("Hii")

# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it

print(Student.college())
print()

#### Important

# 4 pillars -> (Abstraction, Encapsulation, Inheritance, Polymorphism)

# Abstraction -> Hiding the implementation details of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started..")

car1 = Car()
car1.start()



# Encapsulation -> Wrapping data and functions into a single unit (object).

# Let's Practice
# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit method
    def debit(self, amount, comment=""):
        self.comment = comment
        self.balance -= amount
        print(f"Rs {amount} was debited {self.comment}")
        print(f"total balance = {self.get_balance()}")
    
    #credit method
    def credit(self, amount, comment=""):
        self.comment = comment
        self.balance += amount
        print(f"Rs {amount} was credited")
        print(f"total balance = {self.get_balance()}")

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 98765)
# print(acc1.balance)
# print(acc1.account_no)
acc1.debit(2000, "rent")
acc1.credit(700)
print()


# del keyword
# Used to delete object properties or object itself.

# del s1.name
# del s1


class Student:
    def __init__(self, name) -> None:
        self.name = name

s1 = Student("avin")
print(s1)
# del s1
# print(s1)
print(s1.name)
# del s1.name
# print(s1.name)
print()


# Private(like) attributes & methods
# Conceptual Implementations in Python
# Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # add __ to make an attribute private

    def reset__pass(self):  #methods can also be made private by using __ at the start of the method name.
        print(self.__acc_pass)


acc1 = Account("9876", "ask%5")
print(acc1.acc_no)
# print(acc1.acc_pass)
print(acc1.reset__pass())
print()


class Person:
    __name = "kunal"

    def __hello(self):
        print(f"hello {self.__name}!")

    def welcome(self):
        self.__hello()

p1 = Person()
# print(p1.__hello)
# print(p1.__name)
print(p1.welcome())


# Inheritance -> When one class(child/derived) derives the properties & methods of another class(parent/base).

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):   #Single Inheritance
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):  #Multi-level Inheritance
    def __init__(self, type):
        self.type = type

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")
car3 = Fortuner("Diesel")


print(car1.start())
print(car1.color)
car3.start()


# Types of Inheritance

# Single Inheritance -> A single child class is derived from single base(parent) class

# Multi-level Inheritance -> A class derives properties from a class which already derives property from another class. (Multiple child & parent class is available in a single chain)  It can have any level of inheritance.

# Multiple Inheritance -> A single derived class inherites properties from multiple classes.

class A:
    varA = "This is class A."

class B:
    varB = "This is class B."

class C(A, B):
    varC = "This is class C."

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)


# Super Method -> super() method is used to access methods of the parent class.

class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)

car1 = ToyotaCar("prius", "petrol")
print(car1.type)

# Class Method -> A class method is bound to the class & receives the class as an implicit first argument.
# Note - static method can't access or modify class state & generally for utility.

'''
class Student:
    @classmethod    #decorator
    def college(cls):
        pass
'''

class Person:
    name = "anyx"

    def changeName(self, name):
        self.name = name

p1 = Person()
p1.changeName("rahul")
print(p1.name)
print(Person.name)

# Method - 1
class Person:
    name = "anyx"

    def changeName(self, name):
        Person.name = name

p1 = Person()
p1.changeName("rahul")
print(p1.name)
print(Person.name)

# Method - 2
class Person:
    name = "anyx"

    def changeName(self, name):
        self.__class__.name = name

p1 = Person()
p1.changeName("rahul")
print(p1.name)
print(Person.name)

# Method - 3 (use of classmethod)
class Person:
    name = "anyx"

    # def changeName(self, name):
    #     self.name = name

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("rahul")
print(p1.name)
print(Person.name)


# staticmethods (no change)
# classmethods (class)
# instancemethods (self)



# property decorator

class Student:
    def __init__(self, phy, chem, math) -> None:
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.phy)
stu1.calcPercentage()
print(stu1.percentage)


