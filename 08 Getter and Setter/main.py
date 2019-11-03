class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor

        # Disadvantages is the var Not Immediately Changed after reassign new value, solved by using PROPERTY DECORATOR
        # self.info = "Name : {} \n\tHealth : {}\n\tArmor : {}".format(self.name, self.__health, self.__armor)

    @property
    def info(self):
        return "Name : {} \n\tHealth : {}\n\tArmor : {}".format(self.name, self.__health, self.__armor)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, value):
        self.__armor = value

    @armor.deleter
    def armor(self):
        self.__armor = None


kim = Hero("Kim", 100, 20)

# NAME NOT WANT TO CHANGE BECAUSE USING DEFAULT VAR
print(kim.info)
kim.name = "NAME CHANGED"
print(kim.info)

print("*** GETTER ***")
print("Get Armor : ", kim.armor)

# Assign setter is not with the parameter like kim.armor(value) but instead kim.armor = value
print("*** SETTER ***")
kim.armor = 90
print("Get Armor : ", kim.armor)

print("*** DELETER ***")
del kim.armor
print(kim.__dict__)


