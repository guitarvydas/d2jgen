
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

