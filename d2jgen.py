from plib2 import *
def Main ():
    ###in RuleBody
    begin ("Main")
    bpsyn1=declare(False)
    v2=declare(False)
    bp4 = declare (False)
    v3 = declare (None)
    if not bp4:
        v3 = parse_ignoring (lambda :  a ())
        bp4 = not v3
    if not bp4:
        v3 = parse_ignoring (lambda :  b ())
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
