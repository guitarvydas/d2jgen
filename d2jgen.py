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
                    #B PredItem seq4
                    seq4 =  a ()
                    #E PredItem seq4
                    #E BranchingItem -> seq4
                seq3 = seq3 or seq4
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    seq5 = False
                    #B BranchingItem <- seq5
                    #B PredItem seq5
                    seq5 =  b ()
                    #E PredItem seq5
                    #E BranchingItem -> seq5
                seq3 = seq3 or seq5
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
