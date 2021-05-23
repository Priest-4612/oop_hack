"""
Персонаж: class Person Класс, содержащий в себе следующие параметры:

Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты.
Параметры передаются через конструктор;
метод, принимающий на вход список вещей set_things(things);
метод вычитания жизни на основе входной атаки, а также методы для
выполнения алгоритма, представленного ниже;
"""


class Person:
    """
    Персонажи
    """
    def __init__(self, name, hp, base_damage, base_defense):
        self.name = name
        self.hp = hp
        self.base_damage = base_damage
        self.base_defense = base_defense


class Paladin(Person):
    """
    Паладин: class Paladin Класс наследуется от персонажа, при этом количество
    присвоенных жизней и процент защиты умножается на 2 в конструкторе;
    """
    def __init__(self, name, hp, base_damage, base_defense):
        super().__init__(name, hp, base_damage, base_defense)
        self.hp = hp * 2
        self.base_defense = base_defense * 2


class Warrior(Person):
    """
    Воин: class Warrior Класс наследуется от персонажа, при этом атака
    умножается на 2 в конструкторе.
    """
    def __init__(self, name, hp, base_damage, base_defense):
        super().__init__(name, hp, base_damage, base_defense)
        self.base_damage = base_damage * 2
