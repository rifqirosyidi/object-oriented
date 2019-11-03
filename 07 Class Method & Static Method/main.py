class Hero:

    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # This method only apply on a object or instance (self)
    def get_total_obj(self):
        return Hero.__jumlah

    # How About this one? try Hero.get_total()
    def get_total():
        return Hero.__jumlah

    # *** Static Method ***, no args
    @staticmethod
    def get_total_static():
        return Hero.__jumlah

    # *** Class Method ***
    @classmethod
    def get_total_class(cls):
        return cls.__jumlah


rin = Hero("Rin")

gin = Hero("Gir")
wen = Hero("Wen")

# How do we access __jumlah in Hero class variable ? it is private?

# Using static method work on both class adn object
print(Hero.get_total_static())
print(rin.get_total_static())
print(Hero.get_total_class())

