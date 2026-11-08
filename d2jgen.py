
from plib2 import *

def a ():
    begin ("a")
    r1 = True
    if r1:
        r1 = r1 and   b ()
    if r1:
        return accept ("a")
    else:
        return fail ("a")
def c ():
    begin ("c")
    r1 = True
    if r1:
        r1 = r1 and   d ()
    if r1:
        r1 = r1 and   e ()
    if r1:
        return accept ("c")
    else:
        return fail ("c")
def f ():
    begin ("f")
    r1 = True
    
    if r1:
        r1 = r1 and   g ()
    if r1:
        r1 = r1 and   h ()
    if r1:
        return accept ("f")
    else:
        return fail ("f")
def i ():
    begin ("i")
    r1 = True
    r1 =   j ()
    while   j ():
        pass
    if r1:
        return accept ("i")
    else:
        return fail ("i")
def k ():
    begin ("k")
    r1 = True
    while   l ():
        pass
    if r1:
        return accept ("k")
    else:
        return fail ("k")
def m ():
    begin ("m")
    r1 = True
    n ()
    if r1:
        return accept ("m")
    else:
        return fail ("m")

