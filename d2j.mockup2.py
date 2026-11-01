# Manual encoding of the following simple grammar, in Python

# d2j {
#   Main = Array
#   Array = "[" (KV | Object)+ "]"
#   Object = "{" KV+ "}"
#   KV = keystring ":" (Array | Object | string | emptyString | number)
#   string = "\"" (~"\"" any)+ "\""
#   keystring = string
#   emptyString = "\"" "\""
#   number = digit+
#   space += ","
# }



from plib2 import parse, StringBuffer, fail, accept, begin, parse_ignore, parse_string, parse_one_or_more, parse_either, parse_upto, parse_range, parse_set_input, pbuffrepr

##########
## Parser
##########
def s_Main ():
    begin ("s_Main")
    parse_ignore ()
    r = s_Array ()
    if not r: return fail ("s_Main")
    parse_ignore ()
    return accept ("s_Main")

def temp_alt ():
    return parse_either ([s_KV, s_Object])

def s_Array ():
    begin ("s_Array")
    parse_ignore ()
    r = parse_string ("[")
    if not r: return fail ("s_Array")
    parse_ignore ()
    r = parse_one_or_more (temp_alt)
    if not r: return fail ("s_Array")
    parse_ignore ()
    r = parse_string ("]")
    if not r: return fail ("s_Array")
    parse_ignore ()
    return accept ("s_Array")

def s_Object ():
    begin ("s_Object")
    parse_ignore ()
    r = parse_string ("{")
    if not r: return fail ("s_Object")
    parse_ignore ()
    r = parse_one_or_more (s_KV)
    if not r: return fail ("s_Object")
    parse_ignore ()
    r = parse_string ("}")
    if not r: return fail ("s_Object")
    parse_ignore ()
    return accept ("s_Object")

def s_KV ():
    begin ("s_KV")
    parse_ignore ()
    r = l_keystring ()
    if not r: return fail ("s_KV")
    parse_ignore ()
    r = parse_string (":")
    if not r: return fail ("s_KV")
    parse_ignore ()
    r = parse_either ([s_Array, s_Object, l_emptyString, l_string, l_number])
    if not r: return fail ("s_KV")
    parse_ignore ()
    return accept ("s_KV")

def l_string ():
    begin ("l_string")
    r = parse_string ('"')
    if not r: return fail ("l_string")
    r = parse_upto ('"')
    if not r: return fail ("l_string")
    r = parse_string ('"')
    if not r: return fail ("l_string")
    return accept ("l_string")
        
def l_keystring ():
    begin ("l_keystring")
    r = l_string ()
    if not r: return fail ("l_keystring")
    return accept ("l_keystring")

def l_emptyString ():
    begin ("l_emptystring")
    r = parse_string ("\"")
    if not r: return fail ("l_emptyString")
    r = parse_string ("\"")
    if not r: return fail ("l_emptyString")
    return accept ("l_emptystring")

def temp_alt2 ():
    return parse_range ("0", "9")

def l_number ():
    begin ("l_number")
    r = parse_one_or_more (temp_alt2)
    if not r: return fail ("l_number")
    return accept ("l_number")

with open("test.json", "r", encoding="utf-8") as f:
    stest = f.read()
    parse_set_input (stest)
    begin ("test")
    r = s_Array ()
    if (r):
        accept ("test")
        print (f'success')
    else:
        fail ("test")
        print (f'fail')

        
