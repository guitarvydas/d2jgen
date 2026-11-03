from plib2 import parse, StringBuffer, fail, accept, begin, parse_ignore, parse_string, parse_one_or_more, parse_either, parse_upto, parse_range, parse_set_input, pbuffrepr

def main ():
    begin ("main")
    r1 = True
    if r1:
        r1 = r1 and parse_string ("x")
        if r1:
            r1 = r1 and (not parse_string ("y"))
            if r1:
                
                r2 = True;
                if r2:
                    r2 = r2 and parse_string ("a")
                    if r2:
                        
                        r3 = True;
                        if r3:
                            r3 = r3 and parse_string ("g")
                            if r3:
                                r3 = r3 and parse_string ("h")
                                if r3:
                                    r3 = r3 and parse_string ("i");
                        r2 = r2 and r3;
                r1 = r1 and r2
                if r1:
                    r1 = r1 and parse_string ("z")
    if r1:
        return accept ("main")
    else:
        return fail ("main")

with open("test.txt", "r", encoding="utf-8") as f:
    stest = f.read()
    parse_set_input (stest)
    begin ("test")
    if main ():
        accept ("test")
        print (f'success')
    else:
        fail ("test")
        print (f'fail')
