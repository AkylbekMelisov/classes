class Human:

    def __init__(self,name,age,nation,gender):
        self.name = name
        self.age = age
        self.nation = nation
        self.health = 100
        self.documents = []
        self.gender = gender
        self.married = False




    def description(self):
        print(self.name,self.age,self.nation,self.gender,self.health,self.documents)

    def damage(self,number):
        self.health -= number
        if self.health < 0:
            print(f'{self.name} Пора в больницу')

    def set_documents(self,document):
        if self.age > 16 and document == 'pasport':
            self.documents.append(document)
            print(f"{self.name} получить паспорт")
        elif document == 'visa' and self.age > 18:
            self.documents.append(document)
        else:
            print(f"{self.name} не может получить данный докумен!")



human1 = Human('Harry Potter', 10, 'english','male')
human2 = Human('Aigerim', 18,'kyrgyz','female')
# human1.damage(101)
# human1.description()
# human2.health += 1
# human1.set_documents(['pasport','visa','diplom'])
human2.set_documents('pasport')
human2.description()