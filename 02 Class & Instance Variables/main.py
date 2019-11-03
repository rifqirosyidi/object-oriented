class Person:
    # ***** Class Variable / Static Variable
    total_person = 0

    def __init__(self, name, age, phone):
        # ***** Instance / Object Variable
        self.name = name
        self.age = age
        self.phone = phone
        Person.total_person += 1


person1 = Person("RAFI", 20, "085764777")
person2 = Person("RIFQI", 22, "08213219")
person3 = Person("RINA", 19, "098788884")

print(Person.__dict__)
print("")
print(person1.__dict__)

print("TOTAL PERSON : ", Person.total_person)