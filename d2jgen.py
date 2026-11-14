from plib2 import *
def Main ():
    begin ("Main")
    r = True
    if r:
        seq1 = True
        #B SeqItem_preditem <- seq1
        if seq1:
            seq2 = True
            #B PredItem seq2
            seq2 = parse_ignoring (lambda :  number ())
            #E PredItem seq2
            seq1 = seq1 and seq2
        #E SeqItem_preditem -> seq1
        r = r and seq1
    if r:
        return accept ("Main")
    else:
        return fail ("Main")
def number ():
    begin ("number")
    r = True
    if r:
        seq1 = True
        #B SeqItem_alternation <- seq1
        if seq1:
            salt2 = False
            #B AltItem_parenthesized <- salt2
            if salt2:
                alt3 = False
                #B AltItem <- alt3
                if not alt3:
                    alt4 = False
                    #B BranchingItem <- alt4
                    #B PredItem alt4
                    alt4 = parse_string ("0")
                    #E PredItem alt4
                    #E BranchingItem -> alt4
                    alt3 = alt3 or alt4
                #E AltItem -> alt3
                #B AltItem <- alt3
                if not alt3:
                    alt5 = False
                    #B BranchingItem <- alt5
                    #B PredItem alt5
                    alt5 = parse_string ("1")
                    #E PredItem alt5
                    #E BranchingItem -> alt5
                    alt3 = alt3 or alt5
                #E AltItem -> alt3
            salt2 = salt2 or alt3
            #E AltItem_parenthesized -> salt2
            seq1 = seq1 and salt2
        #E SeqItem_alternation -> seq1
        r = r and seq1
    if r:
        return accept ("number")
    else:
        return fail ("number")
