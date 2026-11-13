from plib2 import *
def main ():
    begin ("main")
    r = True
    if r:
        seq1 = True
        if seq1:
            seq2 = True
            #B Alternation_plus <- seq3
            if seq2:
                seq3 = False
                #B AltItem <- seq3
                if not seq3:
                    seq4 = False
                    if seq4:
                        seq5 = True
                        if seq5:
                            seq5 = a ()
                        seq4 = seq4 and seq5
                seq3 = seq3 or seq4
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    seq7 = False
                    if seq7:
                        seq8 = True
                        if seq8:
                            seq8 = b ()
                        seq7 = seq7 and seq8
                seq3 = seq3 or seq7
                #E AltItem -> seq3
            seq2 = seq2 or seq3
            while seq3:
                #B AltItem <- seq3
                if not seq3:
                    seq10 = False
                    if seq10:
                        seq11 = True
                        if seq11:
                            seq11 = a ()
                        seq10 = seq10 and seq11
                seq3 = seq3 or seq10
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    seq13 = False
                    if seq13:
                        seq14 = True
                        if seq14:
                            seq14 = b ()
                        seq13 = seq13 and seq14
                seq3 = seq3 or seq13
                #E AltItem -> seq3
            #E AltItem_pplus -> seq2
            seq1 = seq1 and seq2
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
