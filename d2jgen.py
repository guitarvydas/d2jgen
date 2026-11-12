
from plib2 import *
def main ():
    begin ("main")
    r = True
    a ()undefined  c ()undefined
    if r:
        return accept ("main")
    else:
        return fail ("main")
    
def a ():
    begin ("a")
    r = True
    parse_string ("a")undefined
    if r:
        return accept ("a")
    else:
        return fail ("a")
    
def b ():
    begin ("b")
    r = True
    parse_string ("b")undefined
    if r:
        return accept ("b")
    else:
        return fail ("b")
    
def c ():
    begin ("c")
    r = True
    parse_string ("c")undefined
    if r:
        return accept ("c")
    else:
        return fail ("c")
    

