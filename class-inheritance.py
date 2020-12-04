class Animal:
    cool = True
	
    def make_sound(self, sound):
        #print(f"this animal says {sound}")
        print("this animal says {}".format(sound))
# Cat class inherits from Animal
class Rabbit:
    pass
class Cat(Animal):
    pass
# Make a new cat instance
blue = Cat()
an = Animal()
# Because of inheritance, a Cat has access to:
blue.make_sound("Meow")
print(blue.cool)
#blue is both a Cat and Animal (and base object)
print(isinstance(blue, Cat))
print(isinstance(blue, Animal))
print(isinstance(blue, object)) 
print(isinstance(an, Cat)) 