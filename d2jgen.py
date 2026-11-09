
from plib2 import *
def Main ():
    begin ("Main")
    v1 = True
    v2 = True
    v3 =  parse_ignoring (lambda : parse_string ("{"))
    v2 = v2 and v3
    v1 = v1 and v2
    v4 = True
    v5 = False
    v6 = False
    if not v6:
        v7 = True
        v8 =  parse_ignoring (lambda :  A ())
        v7 = v7 and v8
        v6 = v6 and v7
        
    v9 = False
    if not v9:
        v10 = True
        v11 =  parse_ignoring (lambda :  B ())
        v10 = v10 and v11
        v9 = v9 and v10
        
    v6 = v6 or v9
    v5 = v5 or v6
    v4 = v4 or v5
    v1 = v1 and v4
    v12 = True
    v13 =  parse_ignoring (lambda : parse_string ("}"))
    v12 = v12 and v13
    v1 = v1 and v12
    if v1:
        return accept ("Main")
    else:
        return fail ("Main")
def A ():
    begin ("A")
    v1 = True
    v2 = True
    v3 =  parse_ignoring (lambda : parse_string ("a"))
    v2 = v2 and v3
    v1 = v1 and v2
    if v1:
        return accept ("A")
    else:
        return fail ("A")
def B ():
    begin ("B")
    v1 = True
    v2 = True
    v3 =  parse_ignoring (lambda : parse_string ("b"))
    v2 = v2 and v3
    v1 = v1 and v2
    if v1:
        return accept ("B")
    else:
        return fail ("B")

