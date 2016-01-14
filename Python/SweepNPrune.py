import SquareClass
from SquareClass import *
import LinkedList
from LinkedList import *

def Scanning(lList, main, *argv):
    print ("first normal arg:", main.minX)
    print ("first normal arg:", main.maxX)
    for arg in argv:
        if arg.minX >= main.minX:
            if arg.minX <= main.maxX:
                print ("Collision Detected")
                print (arg.title,"collided with",main.title)
                lList.add(main.title+arg.title)
        else:
            if arg.maxX >= main.minX:
                if arg.maxX <= main.maxX:
                    print ("Collision Detected")
                    print (arg.title,"collided with",main.title)
                    lList.add(main.title+arg.title)
                    print ("another arg through *argv :", arg)
    return lList

myList = LinkedList()
bob = Rectangle(1, 1, 4, 4, 'bob')
bub = Rectangle(2, 2, 6, 6, 'bub')
billy = Rectangle(5, 2, 8, 4, 'billy')
myList = Scanning(myList,bob,bub,billy)
myList = Scanning(myList,bub,billy)
print (myList.get_size())