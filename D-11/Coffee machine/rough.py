# from prettytable import PrettyTable

# table = PrettyTable()
# # print(table)

# table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
# table.add_column("Type",["Electric","Water","Fire"])
# table.align = "r"
# print(table) 

class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} say woof")

    def birthday(self):
        self.age += 1
        print(f"now {self.name} is {self.age} years old")

dog1 = Dog("scooby",50)

dog1.bark()
dog1.birthday()

dog2 = Dog("max",40)
dog2.birthday()

