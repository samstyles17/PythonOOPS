# When to use and when to not use class method and static methods
class Item:
    @staticmethod
    def is_integer():
        pass
    """
    This should be something that has a relationship with the class 
    but not something that must be unique per instance.
    """

    @classmethod
    def instantiate_from_something(cls):
        pass
    """
    This should be something that has a relationship with the class
    , but those are used to manipulate different structures of data to
    instantiate objects, like we have done with CSV.
    """