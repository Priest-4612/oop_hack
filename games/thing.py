"""
Вещи:
class Thing Класс содержит в себе следующие параметры:
    - название,
    - процент защиты,
    - атаку
    - жизнь;
    Это могут быть предметы одежды, магические кольца, всё что угодно)
 """


class Thing:
    """
    Предметы
    """
    def __init__(self, item_name, defense, damage, durability):
        self.item_name = item_name
        self.defense = defense
        self.damage = damage
        self.durability = durability
