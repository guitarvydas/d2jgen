def a () :
    # a = b
    begin ("a")
    v1 = b ()
    if v1:
        return accept ("a")
    else:
        return fail ("a")

def c ():
    # c = d e
    v1 = v1 and d ()
    if v1:
        v1 = v1 and e ()
    if v1:
        return accept ("c")
    else:
        return fail ("c")

def f ():
    # f = (g h)
    v1 = v1 and g ()
    if v1:
        v1 = v1 and h ()
    if v1:
        return accept ("f")
    else:
        return fail ("f")
