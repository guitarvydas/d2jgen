from plib2 import *
def Main ():
    begin ("Main")
    r = True
    seq1 = True
    if r:
        seq1 =  parse_ignoring (lambda :  Array ())
    r = r and seq1
    if r:
        return accept ("Main")
    else:
        return fail ("Main")
def Array ():
    begin ("Array")
    r = True
    seq1 = True
    if r:
        seq1 =  parse_ignoring (lambda : parse_string ("["))
    r = r and seq1
    seq2 = True
    if r:
        (
        seq3 = True
        if seq2:
            seq3 =  parse_ignoring (lambda :  KV ())
        seq2 = seq2 and seq3
        seq4 = True
        if seq2:
            seq4 =  parse_ignoring (lambda :  Object ())
        seq2 = seq2 and seq4
        )+
    r = r and seq2
    seq5 = True
    if r:
        seq5 =  parse_ignoring (lambda : parse_string ("]"))
    r = r and seq5
    if r:
        return accept ("Array")
    else:
        return fail ("Array")
def Object ():
    begin ("Object")
    r = True
    seq1 = True
    if r:
        seq1 =  parse_ignoring (lambda : parse_string ("{"))
    r = r and seq1
    seq2 = True
    if r:
        seq2 =  parse_ignoring (lambda :  KV ())
        r = r and seq2
        while seq2:
            seq2 =  parse_ignoring (lambda :  KV ())
    seq3 = True
    if r:
        seq3 =  parse_ignoring (lambda : parse_string ("}"))
    r = r and seq3
    if r:
        return accept ("Object")
    else:
        return fail ("Object")
def KV ():
    begin ("KV")
    r = True
    seq1 = True
    if r:
        seq1 =  parse_ignoring (lambda :  keystring ())
    r = r and seq1
    seq2 = True
    if r:
        seq2 =  parse_ignoring (lambda : parse_string (":"))
    r = r and seq2
    seq3 = True
    if r:
        (
        seq4 = True
        if seq3:
            seq4 =  parse_ignoring (lambda :  Array ())
        seq3 = seq3 and seq4
        seq5 = True
        if seq3:
            seq5 =  parse_ignoring (lambda :  Object ())
        seq3 = seq3 and seq5
        seq6 = True
        if seq3:
            seq6 =  parse_ignoring (lambda :  string ())
        seq3 = seq3 and seq6
        seq7 = True
        if seq3:
            seq7 =  parse_ignoring (lambda :  emptyString ())
        seq3 = seq3 and seq7
        seq8 = True
        if seq3:
            seq8 =  parse_ignoring (lambda :  number ())
        seq3 = seq3 and seq8
        )
    r = r and seq3
    if r:
        return accept ("KV")
    else:
        return fail ("KV")
def string ():
    begin ("string")
    r = True
    seq1 = True
    if r:
        seq1 =  parse_string ("\"")
    r = r and seq1
    seq2 = True
    if r:
        seq2 =   strchar ()
        r = r and seq2
        while seq2:
            seq2 =   strchar ()
    seq3 = True
    if r:
        seq3 =  parse_string ("\"")
    r = r and seq3
    if r:
        return accept ("string")
    else:
        return fail ("string")
def strchar ():
    begin ("strchar")
    r = True
    seq1 = True
    if r:
        seq1 =  not parse_string ("\"")
    r = r and seq1
    seq2 = True
    if r:
        seq2 =   any ()
    r = r and seq2
    if r:
        return accept ("strchar")
    else:
        return fail ("strchar")
def keystring ():
    begin ("keystring")
    r = True
    seq1 = True
    if r:
        seq1 =   string ()
    r = r and seq1
    if r:
        return accept ("keystring")
    else:
        return fail ("keystring")
def emptyString ():
    begin ("emptyString")
    r = True
    seq1 = True
    if r:
        seq1 =  parse_string ("\"")
    r = r and seq1
    seq2 = True
    if r:
        seq2 =  parse_string ("\"")
    r = r and seq2
    if r:
        return accept ("emptyString")
    else:
        return fail ("emptyString")
def number ():
    begin ("number")
    r = True
    seq1 = True
    if r:
        (
        seq2 = True
        if seq1:
            seq2 =  parse_string ("0")
        seq1 = seq1 and seq2
        seq3 = True
        if seq1:
            seq3 =  parse_string ("1")
        seq1 = seq1 and seq3
        seq4 = True
        if seq1:
            seq4 =  parse_string ("2")
        seq1 = seq1 and seq4
        seq5 = True
        if seq1:
            seq5 =  parse_string ("3")
        seq1 = seq1 and seq5
        seq6 = True
        if seq1:
            seq6 =  parse_string ("4")
        seq1 = seq1 and seq6
        seq7 = True
        if seq1:
            seq7 =  parse_string ("5")
        seq1 = seq1 and seq7
        seq8 = True
        if seq1:
            seq8 =  parse_string ("6")
        seq1 = seq1 and seq8
        seq9 = True
        if seq1:
            seq9 =  parse_string ("7")
        seq1 = seq1 and seq9
        seq10 = True
        if seq1:
            seq10 =  parse_string ("8")
        seq1 = seq1 and seq10
        seq11 = True
        if seq1:
            seq11 =  parse_string ("9")
        seq1 = seq1 and seq11
        )+
    r = r and seq1
    if r:
        return accept ("number")
    else:
        return fail ("number")
