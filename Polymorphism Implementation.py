class Cat:
    def __init__(self , name , age):
        self.name = name
        self.age = age
        

    def info(self):
        print(f"i am a cat. my name is {self.name} i am {self.age} years old ")
        

    def sound(self):
        print("meow")


class Dog:
    def __init__(self , name , age):
        self.name = name
        self.age = age
        

    def info(self):
        print(f"i am a dog. my name is {self.name} i am {self.age} years old ")
        

    def sound(self):
        print("bark")


cat1 = Cat("loez", 5 )

dog1 = Dog("wolf", 2 )

for animal in (dog1,cat1):
    animal.sound()
    animal.info()