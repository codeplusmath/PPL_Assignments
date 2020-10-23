import pygame as pg
import time

pg.mixer.init()
pg.init()
LionS = pg.mixer.Sound("Lion.mp3")
TigerS = pg.mixer.Sound("Tiger.mp3")
ElephantS = pg.mixer.Sound("Elephant.mp3")
CheetahS = pg.mixer.Sound("Cheetah.mp3")
BaboonS = pg.mixer.Sound("Baboon.mp3")
CowS = pg.mixer.Sound("Cow.mp3")
DogS = pg.mixer.Sound("Dog.mp3")
GoatS = pg.mixer.Sound("Goat.mp3")
PigS = pg.mixer.Sound("Pig.mp3")
DonkeyS = pg.mixer.Sound("Donkey.mp3")

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
        print("Symbol of Strength and Courage")
    def sound(self):
        LionS.play()
    def color(self):
        print("Deep Orange-Brown")
    def food(self):
        print("Meat")


class Tiger(wild):
    def special(self):
        print("King of Jungle")
    def sound(self):
        TigerS.play()
    def color(self):
        print("orange")
    def food(self):
        print("Meat")
        

class Elephant(wild):
    def special(self):
        print(" Largest land Animals on Earth")
    def sound(self):
        ElephantS.play()
    def color(self):
        print("Gray")
    def food(self):
        print("Grass")
       
       
class Cheetah(wild):
    def special(self):
        print("Fastest Animal on Earth")
    def sound(self):
        CheetahS.play()
    def color(self):
        print("Tan in color with Black Colored Spots")
    def food(self):
        print("Meat")
        

class Baboon(wild):
    def special(self):
        print("Distinctive Looking Monkeys")
    def sound(self):
        BaboonS.play()
    def color(self):
        print("Brown")
    def food(self):
        print("Grass, Seeds")
        
   
class Cow(domestic):
    def special(self):
        print("Gives milk for Humans")
    def sound(self):
        CowS.play()
    def color(self):
        print("white")
    def food(self):
        print("Grass")
        
        
class Dog(domestic):
    def special(self):
        print("Loyal to Human")
    def sound(self):
        DogS.play()
    def color(self):
        print("Depends on breed (mostly white)")
    def food(self):
        print("Foods of Human")
     
        
        
class Goat(domestic):
    def special(self):
        print("Oldest Domesticated Species of Animal")
    def sound(self):
        GoatS.play()
    def color(self):
        print("Black")
    def food(self):
        print("Grass")
        
        
class pig(domestic):
    def special(self):
        print("Great Sense of Smell")
    def sound(self):
        PigS.play()
    def color(self):
        print("Pink or Black")
    def food(self):
        print("Distillery Waste")
        

class Donkey(wild):
    def special(self):
        print("Load Carriers")
    def sound(self):
        DonkeyS.play()
    def color(self):
        print("white")
    def food(self):
        print("Grass")
        
        
        
        
l1 = Lion()
l1.sound()
t1 = Tiger()
t1.sound()
el1 = Elephant()
el1.sound()
ch1 = Cheetah()
ch1.sound()
b1 = Baboon()
b1.sound()
c1 = Cow()
c1.sound()
d1 = Dog()
d1.sound()
g1 = Goat()
g1.sound()
p1 = Pig()
p1.sound()
d1 = Donkey()
d1.sound()
