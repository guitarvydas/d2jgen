
from plib2 import *
def Main ():
    begin ("Main")
    r = True
    parse_ignoring (lambda :  Array ())
    if r:
        return accept ("Main")
    else:
        return fail ("Main")
    
def Array ():
    begin ("Array")
    r = True
    parse_ignoring (lambda : parse_string ("["))(| parse_ignoring (lambda :  KV ())| parse_ignoring (lambda :  Object ()))+ parse_ignoring (lambda : parse_string ("]"))
    if r:
        return accept ("Array")
    else:
        return fail ("Array")
    
def Object ():
    begin ("Object")
    r = True
    parse_ignoring (lambda : parse_string ("{")) parse_ignoring (lambda :  KV ())+ parse_ignoring (lambda : parse_string ("}"))
    if r:
        return accept ("Object")
    else:
        return fail ("Object")
    
def KV ():
    begin ("KV")
    r = True
    parse_ignoring (lambda :  keystring ()) parse_ignoring (lambda : parse_string (":"))(| parse_ignoring (lambda :  Array ())| parse_ignoring (lambda :  Object ())| parse_ignoring (lambda :  string ())| parse_ignoring (lambda :  emptyString ())| parse_ignoring (lambda :  number ()))
    if r:
        return accept ("KV")
    else:
        return fail ("KV")
    
def string ():
    begin ("string")
    r = True
    parse_string ("\"")  strchar ()+ parse_string ("\"")
    if r:
        return accept ("string")
    else:
        return fail ("string")
    
def strchar ():
    begin ("strchar")
    r = True
    not parse_string ("\"")  any ()
    if r:
        return accept ("strchar")
    else:
        return fail ("strchar")
    
def keystring ():
    begin ("keystring")
    r = True
    string ()
    if r:
        return accept ("keystring")
    else:
        return fail ("keystring")
    
def emptyString ():
    begin ("emptyString")
    r = True
    parse_string ("\"") parse_string ("\"")
    if r:
        return accept ("emptyString")
    else:
        return fail ("emptyString")
    
def number ():
    begin ("number")
    r = True
    (| parse_string ("0")| parse_string ("1")| parse_string ("2")| parse_string ("3")| parse_string ("4")| parse_string ("5")| parse_string ("6")| parse_string ("7")| parse_string ("8")| parse_string ("9"))+
    if r:
        return accept ("number")
    else:
        return fail ("number")
    

