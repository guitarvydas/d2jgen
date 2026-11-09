
from plib2 import *

def main ():
    begin ("main")
    v1 = True
    v2 = True
    
    v3 =  parse_string ("{")
    v2 = v2 and v3
    
    v1 = v1 and v2
    
    v4 = True
    v4 =   a ()
    if v4:
        while   a ():
            pass
    v1 = v1 and v4
    
    v5 = True
    
    v6 =  parse_string ("}")
    v5 = v5 and v6
    
    v1 = v1 and v5
    
    if v1:
        return accept ("main")
    else:
        return fail ("main")
def a ():
    begin ("a")
    v1 = True
    v2 = True
    
    v3 =  parse_string ("a")
    v2 = v2 and v3
    
    v1 = v1 and v2
    
    if v1:
        return accept ("a")
    else:
        return fail ("a")

