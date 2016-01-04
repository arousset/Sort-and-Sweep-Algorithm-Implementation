import rectClass
from rectClass import *
import node&list
from node&list import *

def Scanning(lList, main, *argv):
    print "first min arg:", main.min
    print "first max arg:", main.max
    for arg in argv:
        if arg.min >= main.min:
            if arg.min <= main.max:
                print "Collision Detected"
                print arg.n,"collided with",main.n
                lList.add(main.n+arg.n)
        else:
            if arg.max >= main.min:
                if arg.max <= main.max:
                    print "Collision Detected"
                    print arg.n,"collided with",main.n
                    lList.add(main.n+arg.n)
    return lList