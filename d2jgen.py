
from plib2 import *
def main ():
    begin ("main")
    r = True
    r =   a ()
    if r:
        return accept ("main")
    else:
        return fail ("main")
    
def a ():
    begin ("a")
    r = True
    r =  parse_string ("a")
    if r:
        return accept ("a")
    else:
        return fail ("a")
    

