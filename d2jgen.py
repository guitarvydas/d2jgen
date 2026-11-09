
from plib2 import *

def main ():
    begin ("main")
    v1 = True
    if v1:
        parse_string ("a")
    if v1:
        parse_string ("b")
    if v1:
        
        v1 =  parse_string ("c")
        if v1:
            while  parse_string ("c"):
                pass
    if v1:
        return accept ("main")
    else:
        return fail ("main")

