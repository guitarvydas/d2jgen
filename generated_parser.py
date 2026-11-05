

def string ():
    begin ("string")
    r1 = True
    if r1:
        r1 = r1 and parse_string ("\"")
        if r1:
            
            r2 = True
            if r2:
                r2 = r2 and (not parse_string ("\""))
                if r2:
                    r2 = r2 and any ();
            r1 = r1 and r2
            while
            r3 = True
            if r3:
                r3 = r3 and (not parse_string ("\""))
                if r3:
                    r3 = r3 and any ();
            r1 = r1 and r3:
                pass
            if r1:
                r1 = r1 and parse_string ("\"")
    if r1:
        return accept ("string")
    else:
        return fail ("string")

