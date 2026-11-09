
from plib2 import *
def main ():
    begin ("main")
    v1 = True
    v2 = True
    v3 =  parse_string ("{")
    v2 = v2 and v3
    v1 = v1 and v2
    v4 = True
    v5 = False
    v6 = False
    if not v6:
        v7 = True
        v8 =   a ()
        v7 = v7 and v8
        v6 = v6 and v7
        
    v9 = False
    if not v9:
        v10 = True
        v11 =   b ()
        v10 = v10 and v11
        v9 = v9 and v10
        
    v6 = v6 or v9
    v5 = v5 or v6
    v4 = v4 or v5
    while v5:
        v12 = False
        if not v12:
            v13 = True
            v14 =   a ()
            v13 = v13 and v14
            v12 = v12 and v13
            
        v15 = False
        if not v15:
            v16 = True
            v17 =   b ()
            v16 = v16 and v17
            v15 = v15 and v16
            
        v12 = v12 or v15
        v5 = v5 or v12
        
    v1 = v1 and v4
    v18 = True
    v19 =  parse_string ("}")
    v18 = v18 and v19
    v1 = v1 and v18
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
def b ():
    begin ("b")
    v1 = True
    v2 = True
    v3 =  parse_string ("b")
    v2 = v2 and v3
    v1 = v1 and v2
    if v1:
        return accept ("b")
    else:
        return fail ("b")

