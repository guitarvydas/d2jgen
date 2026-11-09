
from plib2 import *

def main ():
    begin ("main")
    v1 = True
    if v1:
        v1 = v1 and  parse_string ("a")
    if v1:
        v1 = v1 and  parse_string ("b")
    if v1:
        v1 = v1 and  parse_string ("c")
    if v1:
        return accept ("main")
    else:
        return fail ("main")

