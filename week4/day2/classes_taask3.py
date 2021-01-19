class Person:

    def __init__(self,name,health,mana,race):
        self.name = name
        self.health = health
        self.mana = mana
        self.race = race
        self.power = 0
        self.damage = 0
        self.armor = 0
        self.level = 0
        self.exp = 0
        print('Персонаж успешно создан!')


    def description(self):
        print(f"Имя: {self.name}, Здоровье: {self.health}, Мана: {self.mana},Раса: {self.race}, Сила: {self.power}, Урон: {self.damage}, Уровень: {self.level}")

    def level_up(self,exp):
        self.exp += exp
        if self.exp == 100:
            self.level += 1
            choose = input('выберите характеристику')
            if choose == 'power':
                self.power += 1
            elif choose == 'damage':
                self.damage += 1
            elif choose == 'armor':
                self.armor += 1



warrior1 = Person('Tiffany',100,50,'goblin')
warrior1.level_up(100)



warrior1.description()