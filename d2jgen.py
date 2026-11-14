from plib2 import *
def Main ():
    begin ("Main")
    r = declare (True)
    if r:
        seq1 = declare (True)
        #B SeqItem_preditem <- seq1
        if seq1:
            seq2 = declare (True)
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
    r = declare (True)
    if r:
        seq1 = declare (True)
        #B SeqItem_AlternationGroup <- seq1
        if seq1:
            salt2 = declare (False)
            #B AlternationGroup <- salt2
            alt3 = declare (False)
            if salt2:
                #B AltItem <- alt3
                if not alt3:
                    alt4 = declare (False)
                    #B BranchingItem <- alt4
                    #B PredItem alt4
                    alt4 = parse_string ("0")
                    #E PredItem alt4
                    #E BranchingItem -> alt4
                    alt3 = alt3 or alt4
                #E AltItem -> alt3
                #B AltItem <- alt3
                if not alt3:
                    alt5 = declare (False)
                    #B BranchingItem <- alt5
                    #B PredItem alt5
                    alt5 = parse_string ("1")
                    #E PredItem alt5
                    #E BranchingItem -> alt5
                    alt3 = alt3 or alt5
                #E AltItem -> alt3
            salt2 = salt2 or alt3
            #E AlternationGroup -> salt2
            seq1 = seq1 and salt2
        #E SeqItem_AlternationGroup -> seq1
        r = r and seq1
    if r:
        return accept ("number")
    else:
        return fail ("number")
