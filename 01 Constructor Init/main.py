class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone


person1 = Person("RAFI", 20, "085764777")
person2 = Person("RIFQI", 22, "08213219")
person3 = Person("RINA", 19, "098788884")

print(person1.name,
      person1.age,
      person1.phone)

print(person1.__dict__)
print(person2.__dict__)
print(person3.__dict__)
