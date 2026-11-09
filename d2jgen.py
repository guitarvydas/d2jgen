
from plib2 import *

def main ():
    begin ("main")
    v1 = True
    v2 = True
    
    v3 =  parse_string ("\"")
    v2 = v2 and v3
    
    v1 = v1 and v2
    
    v4 = True
    v4 =   strchar ()
    if v4:
        while   strchar ():
            pass
    v1 = v1 and v4
    
    v5 = True
    
    v6 =  parse_string ("\"")
    v5 = v5 and v6
    
    v1 = v1 and v5
    
    if v1:
        return accept ("main")
    else:
        return fail ("main")
def strchar ():
    begin ("strchar")
    v1 = True
    v2 = True
    
    v3 =  not parse_string ("\"")
    v2 = v2 and v3
    
    v1 = v1 and v2
    
    v4 = True
    
    v5 =   any ()
    v4 = v4 and v5
    
    v1 = v1 and v4
    
    if v1:
        return accept ("strchar")
    else:
        return fail ("strchar")

