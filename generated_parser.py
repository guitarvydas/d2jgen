

def Main ():
    begin ("Main")
    r1 = True
    if r1:
        r1 = r1 and Array ()
    if r1:
        return accept ("Main")
    else:
        return fail ("Main")
def Array ():
    begin ("Array")
    r2 = True
    if r2:
        r2 = r2 and parse_string ("[")
        if r2:
            r2 = r2 and KVorObject ()
            while KVorObject ():
                pass
            if r2:
                r2 = r2 and parse_string ("]")
    if r2:
        return accept ("Array")
    else:
        return fail ("Array")
def Object ():
    begin ("Object")
    r3 = True
    if r3:
        r3 = r3 and parse_string ("{")
        if r3:
            r3 = r3 and KV ()
            while KV ():
                pass
            if r3:
                r3 = r3 and parse_string ("}")
    if r3:
        return accept ("Object")
    else:
        return fail ("Object")
def KV ():
    begin ("KV")
    r4 = True
    if r4:
        r4 = r4 and keystring ()
        if r4:
            r4 = r4 and parse_string (":")
            if r4:
                
                r5 = False
                if not r5:
                    r5 = r5 or Array ()
                if not r5:
                    r5 = r5 or Object ()
                if not r5:
                    r5 = r5 or string ()
                if not r5:
                    r5 = r5 or emptyString ()
                if not r5:
                    r5 = r5 or number ();
                r4 = r4 and r5
    if r4:
        return accept ("KV")
    else:
        return fail ("KV")
def KVorObject ():
    begin ("KVorObject")
    r6 = True
    if r6:
        r6 = r6 and KV ()
    if r6:
        r6 = r6 and Object ()
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
            
            r8 = True
            if r8:
                r8 = r8 and (not parse_string ("\""))
                if r8:
                    r8 = r8 and any ();
            r7 = r7 and r8
            while
            r9 = True
            if r9:
                r9 = r9 and (not parse_string ("\""))
                if r9:
                    r9 = r9 and any ();
            r7 = r7 and r9:
                pass
            if r7:
                r7 = r7 and parse_string ("\"")
    if r7:
        return accept ("string")
    else:
        return fail ("string")
def keystring ():
    begin ("keystring")
    r10 = True
    if r10:
        r10 = r10 and string ()
    if r10:
        return accept ("keystring")
    else:
        return fail ("keystring")
def emptyString ():
    begin ("emptyString")
    r11 = True
    if r11:
        r11 = r11 and parse_string ("\"")
        if r11:
            r11 = r11 and parse_string ("\"")
    if r11:
        return accept ("emptyString")
    else:
        return fail ("emptyString")
def digit ():
    begin ("digit")
    r12 = True
    if r12:
        
        r13 = False
        if not r13:
            r13 = r13 or parse_string ("0")
        if not r13:
            r13 = r13 or parse_string ("1")
        if not r13:
            r13 = r13 or parse_string ("2")
        if not r13:
            r13 = r13 or parse_string ("3")
        if not r13:
            r13 = r13 or parse_string ("4")
        if not r13:
            r13 = r13 or parse_string ("5")
        if not r13:
            r13 = r13 or parse_string ("6")
        if not r13:
            r13 = r13 or parse_string ("7")
        if not r13:
            r13 = r13 or parse_string ("8")
        if not r13:
            r13 = r13 or parse_string ("9");
        r12 = r12 and r13
    if r12:
        return accept ("digit")
    else:
        return fail ("digit")
def space ():
    begin ("space")
    r14 = True
    if r14:
        
        r15 = False
        if not r15:
            r15 = r15 or parse_string (",")
        if not r15:
            r15 = r15 or parse_string (" ")
        if not r15:
            r15 = r15 or parse_string ("\n")
        if not r15:
            r15 = r15 or parse_string ("\t");
        r14 = r14 and r15
    if r14:
        return accept ("space")
    else:
        return fail ("space")

