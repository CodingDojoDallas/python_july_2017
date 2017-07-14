class Animal(object):
    def __init__(self, name, health=150):
        self.name = name
        self.health = health

    def walk(self):
        self.health = self.health - 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

    def displayHealth(self):
        print "Animal's health:" + str(self.health)

cat = Animal("kitty", 10)
cat.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health = self.health + 5
        return self

mydog = Dog("sandy")
mydog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
         self.health = self.health - 10
         return self

    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"

dragon1 = Dragon("sparky")
dragon1.fly().displayHealth()
