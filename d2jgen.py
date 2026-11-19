from plib2 import *
def Main ():
    ###in RuleBody
    begin ("Main")
    psyn1=declare(True)
    v2=declare(False)
    v3 = declare (None)
    p6 = declare (True)
    v5 = declare (None)
    if p6:
        v7 = declare (None)
        v7 = parse_ignoring (lambda :  a ())
        v5 = v7
    if p6:
        v9 = declare (None)
        v9 = parse_ignoring (lambda :  b ())
        v5 = v9
    v3 = v5
    p6 = not v5
    v2 = v3
    if v2:
        return accept ("Main")
    else:
        return fail ("Main")
    ###in RuleBody
def a ():
    ###in RuleBody
    begin ("a")
    plex1=declare(True)
    v2=declare(False)
    v3 = declare (None)
    v3 = parse_string ("a")
    v2 = v3
    if v2:
        return accept ("a")
    else:
        return fail ("a")
    ###in RuleBody
def b ():
    ###in RuleBody
    begin ("b")
    plex1=declare(True)
    v2=declare(False)
    v3 = declare (None)
    v3 = parse_string ("b")
    v2 = v3
    if v2:
        return accept ("b")
    else:
        return fail ("b")
    ###in RuleBody
