from plib2 import *
def main ():
    begin ("main")
    r = True
    if r:
        seq1 = True
        if seq1:
            seq2 = True
            if seq2:
                seq3 = True
                if seq3:
                    seq4 = True
                    if seq4:
                        seq4 = a ()
                    if seq4:
                        seq4 = b ()
                    seq3 = seq3 and seq4
                seq2 = seq2 and seq3
            seq1 = seq1 and seq2
            while seq2:
                if seq2:
                    seq7 = True
                    if seq7:
                        seq8 = True
                        if seq8:
                            seq8 = a ()
                        if seq8:
                            seq8 = b ()
                        seq7 = seq7 and seq8
                    seq2 = seq2 and seq7
        if seq1:
            seq1 = c ()
        r = r and seq1
    if r:
        return accept ("main")
    else:
        return fail ("main")
def a ():
    begin ("a")
    r = True
    if r:
        seq1 = True
        if seq1:
            seq2 = parse_string ("a")
            seq1 = seq1 and seq2
        r = r and seq1
    if r:
        return accept ("a")
    else:
        return fail ("a")
def b ():
    begin ("b")
    r = True
    if r:
        seq1 = True
        if seq1:
            seq2 = parse_string ("b")
            seq1 = seq1 and seq2
        r = r and seq1
    if r:
        return accept ("b")
    else:
        return fail ("b")
def c ():
    begin ("c")
    r = True
    if r:
        seq1 = True
        if seq1:
            seq2 = parse_string ("c")
            seq1 = seq1 and seq2
        r = r and seq1
    if r:
        return accept ("c")
    else:
        return fail ("c")
