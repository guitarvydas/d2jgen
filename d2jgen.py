
from plib2 import *

def main ():
    begin ("main")
    v1 = True
    if v1:
        a ()
    if v1:
        d ()
    if v1:
        b ()
    if v1:
        c ()
    if v1:
        return accept ("main")
    else:
        return fail ("main")
def a ():
    begin ("a")
    v1 = True
    if v1: parse_string ("a")
    if v1:
        return accept ("a")
    else:
        return fail ("a")
def b ():
    begin ("b")
    v1 = True
    if v1: parse_string ("b")
    if v1:
        return accept ("b")
    else:
        return fail ("b")
def c ():
    begin ("c")
    v1 = True
    if v1: parse_string ("c")
    if v1:
        return accept ("c")
    else:
        return fail ("c")
def d ():
    begin ("d")
    v1 = True
    if v1: parse_string ("d")
    if v1:
        return accept ("d")
    else:
        return fail ("d")

