from plib2 import *
def Main ():
    ###in RuleBody
    begin ("Main")
    bpsyn1=declare(False)
    v2=declare(False)
    bp4 = declare (False)
    v3 = declare (None)
    if not bp4:
        p6 = declare (False)
        v5 = declare (None)
        if not p6:
            bp8 = declare (False)
            v7 = declare (None)
            if not bp8:
                v7 = parse_ignoring (lambda :  a ())
                bp8 = not v7
            v5 = v7
            p6 = v7
            p6 = v5
        if not p6:
            bp10 = declare (False)
            v9 = declare (None)
            if not bp10:
                v9 = parse_ignoring (lambda :  b ())
                bp10 = not v9
            v5 = v9
            p6 = v9
            p6 = v5
        v3 = v5
        bp4 = p6
        bp4 = not v3
    v2 = v3
    bpsyn1 = v3
    if v2:
        return accept ("Main")
    else:
        return fail ("Main")
    ###in RuleBody
def a ():
    ###in RuleBody
    begin ("a")
    bplex1=declare(False)
    v2=declare(False)
    bp4 = declare (False)
    v3 = declare (None)
    if not bp4:
        v3 = parse_string ("a")
        bp4 = not v3
    v2 = v3
    bplex1 = v3
    if v2:
        return accept ("a")
    else:
        return fail ("a")
    ###in RuleBody
def b ():
    ###in RuleBody
    begin ("b")
    bplex1=declare(False)
    v2=declare(False)
    bp4 = declare (False)
    v3 = declare (None)
    if not bp4:
        v3 = parse_string ("b")
        bp4 = not v3
    v2 = v3
    bplex1 = v3
    if v2:
        return accept ("b")
    else:
        return fail ("b")
    ###in RuleBody
