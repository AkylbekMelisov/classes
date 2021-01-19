class Dog:

    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age
        print(f"{self.name} родился!")

    def sit(self):
        print(f"{self.name} присел!")

    def bring_a_stick(self):
        print(f"{self.name} принеси палку!")

    def jump(self):
        print(f"{self.name} подпрыгнул!")


dog1 = Dog('Hatiko','Husky',10)
dog2 = Dog('strelka','common',6)
print(dog1.name,dog2.name)
dog2.bring_a_stick()
dog1.jump()
