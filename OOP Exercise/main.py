class Hero:

    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def menyerang(self, lawan):  # Self => Current Object
        print(self.name, "menyerang", lawan.name)
        lawan.diserang(self, self.attack)

    def diserang(self, lawan, attack_power_lawan):
        attack_diterima = attack_power_lawan-self.defense
        self.health -= attack_diterima
        print(self.name, "diserang", lawan.name)
        print("serangan diterima : ", str(attack_diterima))
        print("sisa darah", self.name, " : ", str(self.health))


sniper = Hero("Sniper", 150, 25, 5)
archer = Hero("Archer", 150, 25, 10)

sniper.menyerang(archer)
print("\n")
archer.menyerang(sniper)