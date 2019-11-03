class Hero:

    # Class Variable
    total = 0
    __totalPrivate = 0

    def __init__(self, name, health):
        # Instance Var
        self.name = name
        self.health = health

        # Instance Var but Private
        self.__private = "private"

        # Instance Var but Protected
        self._protected = "protected"


rin = Hero("Rin", 200)

print(rin.__dict__)
print(Hero.__dict__)

# Private Var Cannot be Accessed Directly
# print(rin.__private)

