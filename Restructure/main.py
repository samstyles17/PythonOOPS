from item import Item
from phone import Phone

item1 = Item("MyItem", 750)
item2 = Phone('Nokia', 100, 3)
item2.send_email()
item2.apply_increment(0.2)
print(item2.price)
# item1.name = "OtherItem"

# # print(item1.name)
# print(item1.read_only_name)
#
# item1.read_only_name = "BBB"


# Getting an attribute
print(item1.name)

# Setting an attribute
# item1.name = "AAAA0"
# print(item1.name)
item1.apply_increment(0.2)
print(item1.price)
item1.send_email()

"""
@property -> Gives us control of what we want to do with
the attribute and converts the attribute to read-only.
"""

"""
Major OOPS Principles->

1. Encapsulation -> Here, we are making the price attribute read-only.
It is encapsulated inside the class and cannot be changed after 
initialization. We can only modify it through different methods.

2. Abstraction -> Here, send_email() has 3 methods inside it but are abstracted
under send_email(). Also the other methods are private so that they cannot be 
accessed outside the class- level.

abstract methods -> can contain both abstract and concrete 
methods.
concrete classes contain concrete (normal) methods. 


3. Inheritance -> Inherit the methods and attribute of the parent
class. Here, the child class Phone is able to access methods from parent
apply_increment() and send_email().

4. Polymorphism -> One name and many forms. len() is an example of polymorphism. 
It can return the length of the string, list, etc. apply_discount() can be used
in different child classes and override the functionality in the 
child classes.

"""