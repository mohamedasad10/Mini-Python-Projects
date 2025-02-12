#inheritance


class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

        def name(self):
            print(name)


class Cat(Pet):
    def speak(self):
        print("Meow")


p = Cat("Milky",5)        
p.speak()