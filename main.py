import csv


# In python each data type is an object that has been instantiated from some class.
class Item:
    # Class Attributes -> global attributes which belong to a class but can also be accessed by the objects
    pay_rate = 0.8  # The pay rate after 20 % discount
    all = []

    # Constructors in Python -> __init__
    # Collection  of these special methods are called Magic Methods
    # Whenever the object is created the __init__ method is called automatically
    # We pass the specific type in the parameters for validation
    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero !"
        assert quantity >= 0, f"Quantity {price} is not greater than or equal to zero"
        # These are called Instance Attributes
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #     Actions to execute
        Item.all.append(self)

    # Functions declared inside classes are called methods
    # The method will always receive one argument which is the object itself
    def calculate_total_price(self):
        return self.quantity * self.price

    def apply_discount(self):
        # Access the class attributes with class name
        # self.price = self.price * Item.pay_rate
        # Accessing the class attribute inside the method with self , will help in the case of overriding the class attribute or access the class-level attribute
        self.price = self.price * self.pay_rate

    #  When we call the class method, the class object will always be called in the background
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    # Static Method does not need object or class as parameter
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # This method counts out the integers which are point zeroes
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # It's a magic method -> determines how the object is displayed in the console
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


# item1 = Item("Phone", 100, 5)
# # print(item1.name)
# print(item1.calculate_total_price())
# # Accessing the class attributes with the class name
# # Magic attribute -> __dict__ : brings all the attributes which belong to a particular object
# print(Item.__dict__)  # All the attributes of the class- level
# print(item1.__dict__)  # All the attributes of the object- level
#
# item1.apply_discount()

#
# # All the instances of the class are appended in class attribute list all
# print(Item.all)
# for instance in Item.all:
#     print(instance.name)


# Item.instantiate_from_csv()
# print(Item.all)
# print(Item.is_integer(7.5))



