
from plib2 import *

def main ():
    begin ("main")
    v1 = True
    v2 = True
    
    v3 =  parse_string ("a")
    v2 = v2 and v3
    
    v1 = v1 and v2
    
    v4 = True
    
    parse_string ("a")
    v1 = v1 and v4
    
    if v1:
        return accept ("main")
    else:
        return fail ("main")

