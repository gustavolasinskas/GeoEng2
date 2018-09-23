#!/usr/bin/env Python3
#-*-utf-8-*-

class Fruit(object):
    def __init__(self):
        print("I am a fruit!")

    def nutrition(self):
        print ("Fruits have lots of nutrients!")

    def shape(self):
        print("Fruits have all sorts of shapes!")


class Orange(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("I'm an orange!")

    def nutrition(self):
        print("Vitamin C")
    def color(self):
        print("Orange!")
    def shape(self):
        print("Sphere")

f = Fruit()
f.nutrition()
f.shape()

o = Orange()
o.nutrition()
o.shape()
o.color()
