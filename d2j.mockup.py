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



from plib import parse, StringBuffer, fail, accept, begin, parse_ignore, parse_string, parse_one_or_more, parse_either, parse_upto, parse_range, parse_set_input, pbuffrepr

##########
## Parser
##########
def s_Main ():
    begin ("s_Main")
    parse_ignore ()
    if s_Array ():
        parse_ignore ()
        accept ("s_Main")
        return True
    fail ("s_Main")
    return False

def temp_alt ():
    return parse_either ([s_KV, s_Object])

def s_Array ():
    begin ("s_Array")
    parse_ignore ()
    if parse_string ("["):
        parse_ignore ()
        if parse_one_or_more (temp_alt):
            parse_ignore ()
            if parse_string ("]"):
                parse_ignore ()
                accept ("s_Array")
                return True
    fail ("s_Array")
    return False

def s_Object ():
    begin ("s_Object")
    parse_ignore ()
    if parse_string ("{"):
        parse_ignore ()
        if parse_one_or_more (s_KV):
            parse_ignore ()
            if parse_string ("}"):
                parse_ignore ()
                accept ("s_Object")
                return True
    fail ("s_Object")
    return False

def s_KV ():
    begin ("s_KV")
    parse_ignore ()
    if l_keystring ():
        parse_ignore ()
        if parse_string (":"):
            parse_ignore ()
            if parse_either ([s_Array, s_Object, l_emptyString, l_string, l_number]):
                parse_ignore ()
                accept ("s_KV")
                return True
    fail ("s_KV")
    return False

def l_string ():
    begin ("l_string")
    if parse_string ('"'):
        if parse_upto ('"'):
            if parse_string ('"'):
                accept ("l_string")
                return True
    fail ("l_string")
    return False
        
def l_keystring ():
    begin ("l_keystring")
    if l_string ():
        accept ("l_keystring")
        return True
    fail ("l_keystring")
    return False

def l_emptyString ():
    begin ("l_emptystring")
    if parse_string ("\""):
        if parse_string ("\""):
            accept ("l_emptystring")
            return True
    fail ("l_emptystring")
    return False

def temp_alt2 ():
    return parse_range ("0", "9")

def l_number ():
    begin ("l_number")
    if parse_one_or_more (temp_alt2):
        accept ("l_number")
        return True
    fail ("l_number")
    return False


with open("test.json", "r", encoding="utf-8") as f:
    stest = f.read()
    parse_set_input (stest)
    begin ("test")
    if s_Array ():
        accept ("test")
        print (f'success')
    else:
        fail ("test")
        print (f'fail')

        
