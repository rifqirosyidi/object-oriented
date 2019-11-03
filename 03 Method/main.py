class Person:
    # ***** Class Variable / Static Variable
    total_person = 0

    def __init__(self, name, age, phone):
        # ***** Instance / Object Variable
        self.name = name
        self.age = age
        self.phone = phone
        Person.total_person += 1

    # Void Method with no Return
    def show_name(self):
        print("Hello This Object Name is ", self.name)

    # Method with Argument
    def age_up(self, upd):
        self.age += upd

    # Method with return value
    def get_age(self):
        return self.age

person1 = Person("RAFI", 20, "085764777")
person2 = Person("RIFQI", 22, "08213219")
person3 = Person("RINA", 19, "098788884")

person1.show_name()

person1.age_up(1)
print(person1.get_age())

person2.show_name()
