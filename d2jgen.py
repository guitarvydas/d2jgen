
from plib2 import *

def Aa ():
    begin ("Aa")
    r1 = True
    if r1:
        r1 = r1 and  parse_ignoring (lambda :  b ())
    if r1:
        return accept ("Aa")
    else:
        return fail ("Aa")
def Ac ():
    begin ("Ac")
    r1 = True
    if r1:
        r1 = r1 and  parse_ignoring (lambda :  d ())
    if r1:
        r1 = r1 and  parse_ignoring (lambda :  e ())
    if r1:
        return accept ("Ac")
    else:
        return fail ("Ac")
def Af ():
    begin ("Af")
    r1 = True
    
    if r1:
        r1 = r1 and  parse_ignoring (lambda :  g ())
    if r1:
        r1 = r1 and  parse_ignoring (lambda :  h ())
    if r1:
        return accept ("Af")
    else:
        return fail ("Af")
def Ai ():
    begin ("Ai")
    r1 = True
    r1 =  parse_ignoring (lambda :  j ())
    while  parse_ignoring (lambda :  j ()):
        pass
    if r1:
        return accept ("Ai")
    else:
        return fail ("Ai")
def Ak ():
    begin ("Ak")
    r1 = True
    while  parse_ignoring (lambda :  l ()):
        pass
    if r1:
        return accept ("Ak")
    else:
        return fail ("Ak")
def Am ():
    begin ("Am")
    r1 = True
    parse_ignoring (lambda :  n ())
    if r1:
        return accept ("Am")
    else:
        return fail ("Am")

