from plib2 import *
def main ():
    begin ("main")
    r = True
    if r:
        seq1 = True
        #B SeqItem_alternation <- seq2
        if seq1:
            seq2 = True
            #B AltItem_parenthesized <- seq2
            if seq2:
                seq3 = False
                #B AltItem <- seq3
                if not seq3:
                    seq4 = False
                    #B BranchingItem <- seq4
                    if seq4:
                        seq5 = True
                        #B SeqItem_preditem <- seq5
                        if seq5:
                            seq5 = a ()
                        #E SeqItem_preditem -> seq5
                        seq4 = seq4 and seq5
                    #E BranchingItem -> seq4
                seq3 = seq3 or seq4
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    seq7 = False
                    #B BranchingItem <- seq7
                    if seq7:
                        seq8 = True
                        #B SeqItem_preditem <- seq8
                        if seq8:
                            seq8 = b ()
                        #E SeqItem_preditem -> seq8
                        seq7 = seq7 and seq8
                    #E BranchingItem -> seq7
                seq3 = seq3 or seq7
                #E AltItem -> seq3
            seq2 = seq2 or seq3
            #E AltItem_parenthesized -> seq2
            seq1 = seq1 and seq2
        #E SeqItem_alternation -> seq2
        #B SeqItem_preditem <- seq1
        if seq1:
            seq1 = c ()
        #E SeqItem_preditem -> seq1
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
        #B SeqItem_preditem <- seq1
        if seq1:
            seq2 = parse_string ("a")
            #E PredItem seq2
            seq1 = seq1 and seq2
        #E SeqItem_preditem -> seq1
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
        #B SeqItem_preditem <- seq1
        if seq1:
            seq2 = parse_string ("b")
            #E PredItem seq2
            seq1 = seq1 and seq2
        #E SeqItem_preditem -> seq1
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
        #B SeqItem_preditem <- seq1
        if seq1:
            seq2 = parse_string ("c")
            #E PredItem seq2
            seq1 = seq1 and seq2
        #E SeqItem_preditem -> seq1
        r = r and seq1
    if r:
        return accept ("c")
    else:
        return fail ("c")
