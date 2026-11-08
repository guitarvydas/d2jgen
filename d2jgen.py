
from plib2 import *

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

