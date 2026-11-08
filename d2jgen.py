
from plib2 import *

def a ():
    begin ("a")
    v1 = True
    if v1:
        v1 = v1 and   b ()
    if v1:
        return accept ("a")
    else:
        return fail ("a")
def c ():
    begin ("c")
    v1 = True
    if v1:
        v1 = v1 and   d ()
    if v1:
        v1 = v1 and   e ()
    if v1:
        return accept ("c")
    else:
        return fail ("c")

