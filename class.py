'''classes
    what is class
    ordinary vs static classes
    special mehtods
'''
# class = blueprint for making object
# structure = state, constructor, methods
print("===== what is class =====")


class Person ():
    # state
    messege = "class state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # methods
    def introduce(self):
        print(f"hello {self.name}, how are you")

    def say_age(self):
        print(f"{self.name} is {self.age} years old")

    @classmethod
    def explain(cls):
        print("class: static method executed")


person1 = Person("adam", 21)
person2 = Person("marco", 22)
person3 = Person("john", 23)

# ordinary sate
print("person name:", person1.name)
print("person age", person2.age)

# ordinary method
person1.introduce()
person2.say_age()


print("===== ordinary and static properties =====")
# static = class bilan birga keladigan propertylar

# static state
new_messege = Person.messege
print("new messege", new_messege)

# static methods
Person.explain()

print("===== special mehtods =====")
# common special methods
# __init__, __new__, __str__, __call__, __getitem__, __eq__, __len__


class Car():
    # state
    description = "this class makes cars"

    def __new__(cls, *args):
        print("* __new__ *")
        return super().__new__(cls)

    # constructor
    def __init__(self, name, year):
        self.name = name
        self.year = year

    # methods
    def start_engine(self):
        print(f"{self.name} started the engine")

    def stop_engine(self):
        print(f"{self.name} stopped the engine")

    def __str__(self):
        return f"car name: {self.name} was produced in {self.year} year"

    def __call__(self):
        print("object is called like a function")
        return True


my_car = Car("ferrari", 2024)
my_car.start_engine()
my_car.stop_engine()

print("------")
your_car = Car("ferrari", 2020)
print(your_car)
result = your_car()
print("result", result)
