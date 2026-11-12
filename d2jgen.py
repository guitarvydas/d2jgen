
from plib2 import *
def Main ():
    begin ("Main")
    r = True
    Array
    if r:
        return accept ("Main")
    else:
        return fail ("Main")
    
def Array ():
    begin ("Array")
    r = True
    "["(|KV|Object)+"]"
    if r:
        return accept ("Array")
    else:
        return fail ("Array")
    
def Object ():
    begin ("Object")
    r = True
    "{"KV+"}"
    if r:
        return accept ("Object")
    else:
        return fail ("Object")
    
def KV ():
    begin ("KV")
    r = True
    keystring":"(|Array|Object|string|emptyString|number)
    if r:
        return accept ("KV")
    else:
        return fail ("KV")
    
def string ():
    begin ("string")
    r = True
    "\""strchar+"\""
    if r:
        return accept ("string")
    else:
        return fail ("string")
    
def strchar ():
    begin ("strchar")
    r = True
    ~"\""any
    if r:
        return accept ("strchar")
    else:
        return fail ("strchar")
    
def keystring ():
    begin ("keystring")
    r = True
    string
    if r:
        return accept ("keystring")
    else:
        return fail ("keystring")
    
def emptyString ():
    begin ("emptyString")
    r = True
    "\"""\""
    if r:
        return accept ("emptyString")
    else:
        return fail ("emptyString")
    
def number ():
    begin ("number")
    r = True
    (|"0"|"1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9")+
    if r:
        return accept ("number")
    else:
        return fail ("number")
    

