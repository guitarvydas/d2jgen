from plib2 import *
def Main ():
    begin ("Main")
    csyn1=declare(True)
    cseq2 = csyn1
    if cseq2:
        cseq2 =  parse_ignoring (lambda :  a ())
    if cseq2:
        cseq2 =  parse_ignoring (lambda :  b ())
    csyn1 = cseq2
    if csyn1:
        return accept ("Main")
    else:
        return fail ("Main")
def a ():
    begin ("a")
    clex1=declare(True)
    cseq2 = clex1
    if cseq2:
        cseq2 =  parse_string ("a")
    clex1 = cseq2
    if clex1:
        return accept ("a")
    else:
        return fail ("a")
def b ():
    begin ("b")
    clex1=declare(True)
    cseq2 = clex1
    if cseq2:
        cseq2 =  parse_string ("b")
    clex1 = cseq2
    if clex1:
        return accept ("b")
    else:
        return fail ("b")
