class Hero:

    __total = 0

    def __init__(self, name, health, attack, armor):
        self.__name = name
        self.__health_init = health
        self.__attack_init = attack
        self.__armor_init = armor
        self.__level = 1
        self.__exp = 0

        self.__health_max = self.__health_init * self.__level
        self.__attack = self.__attack_init * self.__level
        self.__armor = self.__armor_init * self.__level

        self.__health = self.__health_max

        Hero.__total += 1

    @property
    def gain_exp(self):
        pass

    @gain_exp.setter
    def gain_exp(self, value):
        self.__exp += value
        if self.__exp >= 100:
            print(f'{self.__name} Level Up')
            self.__level += 1
            self.__exp -= 100

            self.__health_max = self.__health_init * self.__level
            self.__attack = self.__attack_init * self.__level
            self.__armor = self.__armor_init * self.__level

    @property
    def info(self):
        return f'Name : {self.__name} \n\t' \
               f'Level : {self.__level}\n\t' \
               f'Health : {self.__health}/{self.__health_max}\n\t' \
               f'Attack : {self.__attack}\n\t' \
               f'Armor : {self.__armor}'

    def attack(self, lawan):
        self.gain_exp = 50


ren = Hero("Ren", 100, 20, 15)
ucup = Hero("Ucup", 100, 10, 25)

print(ren.info)

ren.attack(ucup)
ren.attack(ucup)

print(ren.info)
