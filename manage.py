class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        return "Hello " + self.name, "my age is " + str(self.age)


p = Person("Jahongir", 2022-1993)
print(p.func())
