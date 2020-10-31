import winsound


class animal:
    def __init__(self , legs=4, eyes=2, tail=1):
        self.legs=legs
        self.eyes=eyes
        
     
class wild(animal):
    def habitat(self):
        print("In Jungle")
        
        
class domestic(animal):
    def habitat(self):
        print("Among Human")
        
        
class Lion(wild):
    def special(self):
        print("Known As : Symbol of Strength and Courage")
    def sound(self):
        print("Lion's Sound is playing")
        winsound.PlaySound("Lion.wav", winsound.SND_FILENAME)
    def color(self):
        print("Deep Orange-Brown")
    def food(self):
        print("Meat")


class Tiger(wild):
    def special(self):
        print("Known As : King of Jungle")
    def sound(self):
        print("Tiger's Sound is playing")
        winsound.PlaySound("Tiger.wav", winsound.SND_FILENAME)
    def color(self):
        print("orange")
    def food(self):
        print("Meat")
        

class Elephant(wild):
    def special(self):
        print("Known As : Largest land Animals on Earth")
    def sound(self):
        print("Elephant's Sound is playing")
        winsound.PlaySound("Elephant.wav", winsound.SND_FILENAME)
    def color(self):
        print("Gray")
    def food(self):
        print("Grass")
       
       
class Cheetah(wild):
    def special(self):
        print("Known As : Fastest Animal on Earth")
    def sound(self):
        print("Cheetah's Sound is playing")
        winsound.PlaySound("Cheetah.wav", winsound.SND_FILENAME)
    def color(self):
        print("Tan in color with Black Colored Spots")
    def food(self):
        print("Meat")
        

class Baboon(wild):
    def special(self):
        print("Known As : Distinctive Looking Monkeys")
    def sound(self):
        print("Baboon's Sound is playing")
        winsound.PlaySound("Baboon.wav", winsound.SND_FILENAME)
    def color(self):
        print("Brown")
    def food(self):
        print("Grass, Seeds")
        
   
class Cow(domestic):
    def special(self):
        print("Known As : Gives milk for Humans")
    def sound(self):
        print("Cow's Sound is playing")
        winsound.PlaySound("Cow.wav", winsound.SND_FILENAME)
    def color(self):
        print("white")
    def food(self):
        print("Grass")
        
        
class Dog(domestic):
    def special(self):
        print("Known As : Loyal to Human")
    def sound(self):
        print("Dog's Sound is playing")
        winsound.PlaySound("Dog.wav", winsound.SND_FILENAME)
    def color(self):
        print("Depends on breed (mostly white)")
    def food(self):
        print("Foods of Human")
     
        
        
class Goat(domestic):
    def special(self):
        print("Known As : Oldest Domesticated Species of Animal")
    def sound(self):
        print("Goat's Sound is playing")
        winsound.PlaySound("Goat.wav", winsound.SND_FILENAME)
    def color(self):
        print("Black")
    def food(self):
        print("Grass")
        
        
class Pig(domestic):
    def special(self):
        print("Known As : Great Sense of Smell")
    def sound(self):
        print("Pig's Sound is playing")
        winsound.PlaySound("Pig.wav", winsound.SND_FILENAME)
    def color(self):
        print("Pink or Black")
    def food(self):
        print("Distillery Waste")
        

class Donkey(wild):
    def special(self):
        print("Known As : Load Carriers")
    def sound(self):
        print("Donkey's Sound is playing")
        winsound.PlaySound("Donkey.wav", winsound.SND_FILENAME)
    def color(self):
        print("white")
    def food(self):
        print("Grass")
        
        
        
        
l1 = Lion()
l1.sound()
l1.special()
print("")
print("")
t1 = Tiger()
t1.sound()
t1.special()
print("")
print("")
el1 = Elephant()
el1.sound()
el1.special()
print("")
print("")
ch1 = Cheetah()
ch1.sound()
ch1.special()
print("")
print("")
b1 = Baboon()
b1.sound()
b1.special()
print("")
print("")
c1 = Cow()
c1.sound()
c1.special()
print("")
print("")
d1 = Dog()
d1.sound()
d1.special()
print("")
print("")
g1 = Goat()
g1.sound()
g1.special()
print("")
print("")
p1 = Pig()
p1.sound()
p1.special()
print("")
print("")
do1 = Donkey()
do1.sound()
do1.special()
print("")