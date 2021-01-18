class Car:

    def __init__(self,mark, color,model,year):
        self.mark = mark
        self.color = color
        self.model = model
        self.year = year
        self.run = 0
        self.engine = ''
        self.boost = 0  #измеряется в секундах, разгон до 100 км/ч

    def move(self,distance:int):
        if distance > 0:
            self.run += distance

    def set_engine(self,new_engine):
        self.engine = new_engine
        if new_engine == 'common':
            self.boost = 7
        elif new_engine == 'advance':
            self.boost = 4
        elif new_engine == 'race':
            self.boost = 2

car1 = Car('bmv','back','x6','2020')
car2 = Car('mercedes','pink','s 600','2021')
car3 = Car('tesla','white','S 6','2021')
car3.move(240)
print(car3.mark,car3.model,car3.run)
car3.move(-240)
print(car3.mark,car3.model,car3.run)
car3.set_engine('advanced')
print(car2.engine,car2.boost)
print(car3.engine,car3.boost)

