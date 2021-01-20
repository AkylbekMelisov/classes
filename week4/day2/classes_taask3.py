class Person:

    def __init__(self,name,health,mana,race):
        self.name = name
        self.race = race
        if self.race == 'fary':
            self.health = 10
            self.mana = 2000
        elif self.race == 'goblin':
            self.health = 200
            self.mana = 100
        else:
            self.health = 150
            self.mana = 150
        self.health = health
        self.mana = mana
        self.power = 0
        self.damage = 0
        self.armor = 0
        self.level = 0
        self.exp = 0
        print('Персонаж успешно создан!')


    def description(self):
        print(f"Имя: {self.name}, Здоровье: {self.health}, Мана: {self.mana},Раса: {self.race}, Сила: {self.power}, Урон: {self.damage}, Уровень: {self.level} Броня: {self.armor}")

    def level_up(self,exp):
        self.exp += exp
        if self.exp == 100:
            self.level += 100 // 20
            self.power += 100 // 20
            self.damage += 100 // 20
            self.armor += 100 // 20

    def wear(self,cloth):
        if cloth == 'pentaarmor':
            self.armor += 20
        elif cloth == 'legendary dress':
            self.armor += 100
            self.health += 50
        elif cloth == 'witch jacet':
            self.mana += 100
        elif cloth == 'legendary plate':
            self.mana += 20
            self.armor += 500
            self.health += 200

    def set_weapon(self,weapon):
        if weapon == 'sword':
            self.power += 1
        elif weapon == 'axe':
            self.power += 1
            self.damage += 2
        elif weapon == 'bow':
            self.power += 1
            self.damage += 3
            self.mana +=  5



warrior1 = Person('Tiffany',100,50,'goblin')
warrior1.level_up(100)
warrior1.wear('legendary plate')




warrior1.description()