from plib2 import *
def main ():
    begin ("main")
    r = True
    if r:
        seq1 = True
        if seq1:
            seq2 = True
            if seq2:
                seq2 = a ()
            if seq2:
                seq2 = b ()
            seq1 = seq1 and seq2
        r = r and seq1
        while seq1:
            if seq1:
                seq5 = True
                if seq5:
                    seq5 = a ()
                if seq5:
                    seq5 = b ()
                seq1 = seq1 and seq5
    if r:
        r = c ()
    if r:
        return accept ("main")
    else:
        return fail ("main")
def a ():
    begin ("a")
    r = True
    if r:
        seq1 = parse_string ("a")
        r = r and seq1
    if r:
        return accept ("a")
    else:
        return fail ("a")
def b ():
    begin ("b")
    r = True
    if r:
        seq1 = parse_string ("b")
        r = r and seq1
    if r:
        return accept ("b")
    else:
        return fail ("b")
def c ():
    begin ("c")
    r = True
    if r:
        seq1 = parse_string ("c")
        r = r and seq1
    if r:
        return accept ("c")
    else:
        return fail ("c")
