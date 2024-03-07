class Student:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Name->{self.name}, Age -> {self.age}"


s1 = Student("Harsh", 24)
print(s1)
