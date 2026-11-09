
from plib2 import *
def main ():
    begin ("main")
    v1 = True
    v2 = True
    v3 =  parse_string ("{")
    v2 = v2 and v3
    v1 = v1 and v2
    v4 = True
    v5 = True
    v6 =   a ()
    v5 = v5 and v6
    v4 = v4 and v5
    v1 = v1 and v4
    v7 = True
    v8 =  parse_string ("}")
    v7 = v7 and v8
    v1 = v1 and v7
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

