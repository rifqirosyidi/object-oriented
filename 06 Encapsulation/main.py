# Encapsulation : All Var is Private
# to get the data is using getter and setter


class Hero:

    def __init__(self, name, health, attack):
        self.__name = name
        self.__health = health
        self.__attack = attack

    # *** GETTER ***
    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    # *** SETTER ***
    def attacked(self, value):
        self.__health -= value

    def attack_up(self, value):
        self.__attack = value


earth_shaker = Hero("Earth Shaker", 90, 10)

print(earth_shaker.get_name())
print(earth_shaker.get_health())
earth_shaker.attacked(5)
print(earth_shaker.get_health())

