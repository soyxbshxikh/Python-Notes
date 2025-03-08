class Animal:
    def __init__(self,name):
        self.name = name
    
    def speaks():
        pass

class Dog(Animal):
    def speaks(self):
        return f'{self.name} barks !!'
    
class Cat(Animal):
    def speaks(self):
        return f'{self.name} barks !!'
    
dog = Dog('Tommy')
print(dog.speaks())

cat = Cat('Kitty')
print(cat.speaks())
    
