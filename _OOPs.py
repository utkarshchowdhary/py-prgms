# Objects are defined by characteristics and actions
# A characteristic would be a noun. On the other hand, an action would be a verb

"""
Object-Oriented Programming (OOP) Vocabulary
"""
# class - a blueprint consisting of methods and attributes
# object - an instance of a class.
# attribute - a descriptor or characteristic
# method - an action that a class or object could take

# encapsulation: you can combine functions and data all into a single entity.
# In object-oriented programming, this single entity is called a class.
# Encapsulation allows you to hide implementation details

# The difference between function and method is that method is inside of a
# class whereas a function is outside of a class.

# self represents the instance of the class. By using the “self” keyword we can access
# the attributes and methods of the class in python
"""
class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
    
    def change_price(self, new_price):
        self.price = new_price
        
    def discount(self, discount):
        return self.price * (1 - discount)

new_shirt = Shirt('red, 'S', 'short sleeve', 15)
print(new_shirt.color,new_shirt.size,new_shirt.style,new_shirt.price) //red S short sleeve 15
new_shirt.change_price(10)
print(new_shirt.price) //10
print(new_shirt.discount(0.2)) //0.8

"""
## Dunder or magic methods
# Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name
# The __init__ method for initialization is invoked without any call, when an instance of a class is created

# Inheritance helps organize code with a more general version of a class and then specific children
