
from plib2 import *

def Main ():
    begin ("Main")
    r1 = True
    if r1:
        r1 = r1 and parse_ignoring (lambda : KVorObject ())
    if r1:
        return accept ("Main")
    else:
        return fail ("Main")
def Array ():
    begin ("Array")
    r2 = True
    if r2:
        r2 = r2 and parse_ignoring (lambda : parse_string ("["))
        if r2:
            r2 = r2 and parse_ignoring (lambda : KVorObject ())
            while parse_ignoring (lambda : KVorObject ()):
                pass
            if r2:
                r2 = r2 and parse_ignoring (lambda : parse_string ("]"))
    if r2:
        return accept ("Array")
    else:
        return fail ("Array")
def Object ():
    begin ("Object")
    r3 = True
    if r3:
        r3 = r3 and parse_ignoring (lambda : parse_string ("{"))
        if r3:
            r3 = r3 and parse_ignoring (lambda : KV ())
            while parse_ignoring (lambda : KV ()):
                pass
            if r3:
                r3 = r3 and parse_ignoring (lambda : parse_string ("}"))
    if r3:
        return accept ("Object")
    else:
        return fail ("Object")
def KV ():
    begin ("KV")
    r4 = True
    if r4:
        r4 = r4 and parse_ignoring (lambda : keystring ())
        if r4:
            r4 = r4 and parse_ignoring (lambda : parse_string (":"))
            if r4:
                r4 = r4 and parse_ignoring (lambda : AOsen ())
    if r4:
        return accept ("KV")
    else:
        return fail ("KV")
def AOsen ():
    begin ("AOsen")
    r5 = True
    if r5:
        r5 = r5 and parse_ignoring (lambda : Array ())
    if r5:
        r5 = r5 and parse_ignoring (lambda : Object ())
    if r5:
        r5 = r5 and parse_ignoring (lambda : string ())
    if r5:
        r5 = r5 and parse_ignoring (lambda : emptyString ())
    if r5:
        r5 = r5 and parse_ignoring (lambda : number ())
    if r5:
        return accept ("AOsen")
    else:
        return fail ("AOsen")
def KVorObject ():
    begin ("KVorObject")
    r6 = True
    if r6:
        r6 = r6 and parse_ignoring (lambda : KV ())
    if r6:
        r6 = r6 and parse_ignoring (lambda : Object ())
    if r6:
        return accept ("KVorObject")
    else:
        return fail ("KVorObject")
def string ():
    begin ("string")
    r7 = True
    if r7:
        r7 = r7 and parse_string ("\"")
        if r7:
            r7 = r7 and strchar ()
            while strchar ():
                pass
            if r7:
                r7 = r7 and parse_string ("\"")
    if r7:
        return accept ("string")
    else:
        return fail ("string")
def strchar ():
    begin ("strchar")
    r8 = True
    if r8:
        r8 = r8 and (not parse_string ("\""))
        if r8:
            r8 = r8 and any ()
    if r8:
        return accept ("strchar")
    else:
        return fail ("strchar")
def keystring ():
    begin ("keystring")
    r9 = True
    if r9:
        r9 = r9 and string ()
    if r9:
        return accept ("keystring")
    else:
        return fail ("keystring")
def emptyString ():
    begin ("emptyString")
    r10 = True
    if r10:
        r10 = r10 and parse_string ("\"")
        if r10:
            r10 = r10 and parse_string ("\"")
    if r10:
        return accept ("emptyString")
    else:
        return fail ("emptyString")
def number ():
    begin ("number")
    r11 = True
    if r11:
        r11 = r11 and ndigit ()
        while ndigit ():
            pass
    if r11:
        return accept ("number")
    else:
        return fail ("number")
def ndigit ():
    begin ("ndigit")
    r12 = True
    if r12:
        r12 = r12 and parse_string ("0")
    if r12:
        r12 = r12 and parse_string ("1")
    if r12:
        r12 = r12 and parse_string ("2")
    if r12:
        r12 = r12 and parse_string ("3")
    if r12:
        r12 = r12 and parse_string ("4")
    if r12:
        r12 = r12 and parse_string ("5")
    if r12:
        r12 = r12 and parse_string ("6")
    if r12:
        r12 = r12 and parse_string ("7")
    if r12:
        r12 = r12 and parse_string ("8")
    if r12:
        r12 = r12 and parse_string ("9")
    if r12:
        return accept ("ndigit")
    else:
        return fail ("ndigit")
def ws ():
    begin ("ws")
    r13 = True
    if r13:
        r13 = r13 and parse_string (",")
    if r13:
        r13 = r13 and parse_string (" ")
    if r13:
        r13 = r13 and parse_string ("\n")
    if r13:
        r13 = r13 and parse_string ("\t")
    if r13:
        return accept ("ws")
    else:
        return fail ("ws")

