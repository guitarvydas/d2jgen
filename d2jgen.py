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
            seq2 = parse_ignoring (lambda :  Array ())
            #E PredItem seq2
            seq1 = seq1 and seq2
        #E SeqItem_preditem -> seq1
        r = r and seq1
    if r:
        return accept ("Main")
    else:
        return fail ("Main")
def Array ():
    begin ("Array")
    r = declare (True)
    if r:
        seq1 = declare (True)
        #B SeqItem_preditem <- seq1
        if seq1:
            seq2 = declare (True)
            #B PredItem seq2
            seq2 = parse_ignoring (lambda : parse_string ("["))
            #E PredItem seq2
            seq1 = seq1 and seq2
        #E SeqItem_preditem -> seq1
        #B SeqItem_sequence <- seq1
        if seq1:
            seq3 = declare (True)
            if seq3:
                seq4 = declare (True)
                #B SeqItem_AlternationGroup <- seq4
                if seq4:
                    #B AlternationGroup_plus <- seqalt5
                    if seqalt5:
                        seq6 = declare (False)
                        #B AltItem <- seq6
                        if not seq6:
                            alt7 = declare (False)
                            #B BranchingItem <- alt7
                            #B PredItem alt7
                            alt7 = parse_ignoring (lambda :  KV ())
                            #E PredItem alt7
                            #E BranchingItem -> alt7
                            seq6 = seq6 or alt7
                        #E AltItem -> seq6
                        #B AltItem <- seq6
                        if not seq6:
                            alt8 = declare (False)
                            #B BranchingItem <- alt8
                            #B PredItem alt8
                            alt8 = parse_ignoring (lambda :  Object ())
                            #E PredItem alt8
                            #E BranchingItem -> alt8
                            seq6 = seq6 or alt8
                        #E AltItem -> seq6
                        seqalt5 = seqalt5 or seq6
                    while seq6:
                        #B AltItem <- seq6
                        if not seq6:
                            alt9 = declare (False)
                            #B BranchingItem <- alt9
                            #B PredItem alt9
                            alt9 = parse_ignoring (lambda :  KV ())
                            #E PredItem alt9
                            #E BranchingItem -> alt9
                            seq6 = seq6 or alt9
                        #E AltItem -> seq6
                        #B AltItem <- seq6
                        if not seq6:
                            alt10 = declare (False)
                            #B BranchingItem <- alt10
                            #B PredItem alt10
                            alt10 = parse_ignoring (lambda :  Object ())
                            #E PredItem alt10
                            #E BranchingItem -> alt10
                            seq6 = seq6 or alt10
                        #E AltItem -> seq6
                    #E AltItem_pplus -> seqalt5
                    seq4 = seq4 and seqalt5
                    seqalt5 = declare (False)
                #E SeqItem_AlternationGroup -> seq4
                #B SeqItem_preditem <- seq4
                if seq4:
                    seq11 = declare (True)
                    #B PredItem seq11
                    seq11 = parse_ignoring (lambda : parse_string ("]"))
                    #E PredItem seq11
                    seq4 = seq4 and seq11
                #E SeqItem_preditem -> seq4
                seq3 = seq3 and seq4
            seq1 = seq1 and seq3
        #E SeqItem_sequence -> seq1
        r = r and seq1
    if r:
        return accept ("Array")
    else:
        return fail ("Array")
def Object ():
    begin ("Object")
    r = declare (True)
    if r:
        seq1 = declare (True)
        #B SeqItem_preditem <- seq1
        if seq1:
            seq2 = declare (True)
            #B PredItem seq2
            seq2 = parse_ignoring (lambda : parse_string ("{"))
            #E PredItem seq2
            seq1 = seq1 and seq2
        #E SeqItem_preditem -> seq1
        #B SeqItem_sequence <- seq1
        if seq1:
            seq3 = declare (True)
            if seq3:
                seq4 = declare (True)
                #B SeqItem_preditemplus <- seq4
                if seq4:
                    seq5 = declare (True)
                    #B PredItem seq5
                    seq5 = parse_ignoring (lambda :  KV ())
                    #E PredItem seq5
                    seq4 = seq4 and seq5
                    while seq5:
                        #B PredItem seq5
                        seq5 = parse_ignoring (lambda :  KV ())
                        #E PredItem seq5
                #E SeqItem_preditemplus -> seq4
                #B SeqItem_preditem <- seq4
                if seq4:
                    seq6 = declare (True)
                    #B PredItem seq6
                    seq6 = parse_ignoring (lambda : parse_string ("}"))
                    #E PredItem seq6
                    seq4 = seq4 and seq6
                #E SeqItem_preditem -> seq4
                seq3 = seq3 and seq4
            seq1 = seq1 and seq3
        #E SeqItem_sequence -> seq1
        r = r and seq1
    if r:
        return accept ("Object")
    else:
        return fail ("Object")
def KV ():
    begin ("KV")
    r = declare (True)
    if r:
        seq1 = declare (True)
        #B SeqItem_preditem <- seq1
        if seq1:
            seq2 = declare (True)
            #B PredItem seq2
            seq2 = parse_ignoring (lambda :  keystring ())
            #E PredItem seq2
            seq1 = seq1 and seq2
        #E SeqItem_preditem -> seq1
        #B SeqItem_sequence <- seq1
        if seq1:
            seq3 = declare (True)
            if seq3:
                seq4 = declare (True)
                #B SeqItem_preditem <- seq4
                if seq4:
                    seq5 = declare (True)
                    #B PredItem seq5
                    seq5 = parse_ignoring (lambda : parse_string (":"))
                    #E PredItem seq5
                    seq4 = seq4 and seq5
                #E SeqItem_preditem -> seq4
                #B SeqItem_AlternationGroup <- seq4
                if seq4:
                    #B AlternationGroup <- seqalt6
                    alt7 = declare (False)
                    if seqalt6:
                        #B AltItem <- alt7
                        if not alt7:
                            alt8 = declare (False)
                            #B BranchingItem <- alt8
                            #B PredItem alt8
                            alt8 = parse_ignoring (lambda :  Array ())
                            #E PredItem alt8
                            #E BranchingItem -> alt8
                            alt7 = alt7 or alt8
                        #E AltItem -> alt7
                        #B AltItem <- alt7
                        if not alt7:
                            alt9 = declare (False)
                            #B BranchingItem <- alt9
                            #B PredItem alt9
                            alt9 = parse_ignoring (lambda :  Object ())
                            #E PredItem alt9
                            #E BranchingItem -> alt9
                            alt7 = alt7 or alt9
                        #E AltItem -> alt7
                        #B AltItem <- alt7
                        if not alt7:
                            alt10 = declare (False)
                            #B BranchingItem <- alt10
                            #B PredItem alt10
                            alt10 = parse_ignoring (lambda :  string ())
                            #E PredItem alt10
                            #E BranchingItem -> alt10
                            alt7 = alt7 or alt10
                        #E AltItem -> alt7
                        #B AltItem <- alt7
                        if not alt7:
                            alt11 = declare (False)
                            #B BranchingItem <- alt11
                            #B PredItem alt11
                            alt11 = parse_ignoring (lambda :  emptyString ())
                            #E PredItem alt11
                            #E BranchingItem -> alt11
                            alt7 = alt7 or alt11
                        #E AltItem -> alt7
                        #B AltItem <- alt7
                        if not alt7:
                            alt12 = declare (False)
                            #B BranchingItem <- alt12
                            #B PredItem alt12
                            alt12 = parse_ignoring (lambda :  number ())
                            #E PredItem alt12
                            #E BranchingItem -> alt12
                            alt7 = alt7 or alt12
                        #E AltItem -> alt7
                    seqalt6 = seqalt6 or alt7
                    #E AlternationGroup -> seqalt6
                    seq4 = seq4 and seqalt6
                    seqalt6 = declare (False)
                #E SeqItem_AlternationGroup -> seq4
                seq3 = seq3 and seq4
            seq1 = seq1 and seq3
        #E SeqItem_sequence -> seq1
        r = r and seq1
    if r:
        return accept ("KV")
    else:
        return fail ("KV")
def string ():
    begin ("string")
    r = declare (True)
    if r:
        seq1 = declare (True)
        #B SeqItem_preditem <- seq1
        if seq1:
            seq2 = declare (True)
            #B PredItem seq2
            seq2 = parse_string ("\"")
            #E PredItem seq2
            seq1 = seq1 and seq2
        #E SeqItem_preditem -> seq1
        #B SeqItem_sequence <- seq1
        if seq1:
            seq3 = declare (True)
            if seq3:
                seq4 = declare (True)
                #B SeqItem_preditemplus <- seq4
                if seq4:
                    seq5 = declare (True)
                    #B PredItem seq5
                    seq5 =  strchar ()
                    #E PredItem seq5
                    seq4 = seq4 and seq5
                    while seq5:
                        #B PredItem seq5
                        seq5 =  strchar ()
                        #E PredItem seq5
                #E SeqItem_preditemplus -> seq4
                #B SeqItem_preditem <- seq4
                if seq4:
                    seq6 = declare (True)
                    #B PredItem seq6
                    seq6 = parse_string ("\"")
                    #E PredItem seq6
                    seq4 = seq4 and seq6
                #E SeqItem_preditem -> seq4
                seq3 = seq3 and seq4
            seq1 = seq1 and seq3
        #E SeqItem_sequence -> seq1
        r = r and seq1
    if r:
        return accept ("string")
    else:
        return fail ("string")
def strchar ():
    begin ("strchar")
    r = declare (True)
    if r:
        seq1 = declare (True)
        #B SeqItem_preditem <- seq1
        if seq1:
            seq2 = declare (True)
            #B PredItem seq2
            seq2 = not parse_string ("\"")
            #E PredItem seq2
            seq1 = seq1 and seq2
        #E SeqItem_preditem -> seq1
        #B SeqItem_preditem <- seq1
        if seq1:
            seq3 = declare (True)
            #B PredItem seq3
            seq3 =  any ()
            #E PredItem seq3
            seq1 = seq1 and seq3
        #E SeqItem_preditem -> seq1
        r = r and seq1
    if r:
        return accept ("strchar")
    else:
        return fail ("strchar")
def keystring ():
    begin ("keystring")
    r = declare (True)
    if r:
        seq1 = declare (True)
        #B SeqItem_preditem <- seq1
        if seq1:
            seq2 = declare (True)
            #B PredItem seq2
            seq2 =  string ()
            #E PredItem seq2
            seq1 = seq1 and seq2
        #E SeqItem_preditem -> seq1
        r = r and seq1
    if r:
        return accept ("keystring")
    else:
        return fail ("keystring")
def emptyString ():
    begin ("emptyString")
    r = declare (True)
    if r:
        seq1 = declare (True)
        #B SeqItem_preditem <- seq1
        if seq1:
            seq2 = declare (True)
            #B PredItem seq2
            seq2 = parse_string ("\"")
            #E PredItem seq2
            seq1 = seq1 and seq2
        #E SeqItem_preditem -> seq1
        #B SeqItem_preditem <- seq1
        if seq1:
            seq3 = declare (True)
            #B PredItem seq3
            seq3 = parse_string ("\"")
            #E PredItem seq3
            seq1 = seq1 and seq3
        #E SeqItem_preditem -> seq1
        r = r and seq1
    if r:
        return accept ("emptyString")
    else:
        return fail ("emptyString")
def number ():
    begin ("number")
    r = declare (True)
    if r:
        seq1 = declare (True)
        #B SeqItem_AlternationGroup <- seq1
        if seq1:
            #B AlternationGroup_plus <- seqalt2
            if seqalt2:
                seq3 = declare (False)
                #B AltItem <- seq3
                if not seq3:
                    alt4 = declare (False)
                    #B BranchingItem <- alt4
                    #B PredItem alt4
                    alt4 = parse_string ("0")
                    #E PredItem alt4
                    #E BranchingItem -> alt4
                    seq3 = seq3 or alt4
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt5 = declare (False)
                    #B BranchingItem <- alt5
                    #B PredItem alt5
                    alt5 = parse_string ("1")
                    #E PredItem alt5
                    #E BranchingItem -> alt5
                    seq3 = seq3 or alt5
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt6 = declare (False)
                    #B BranchingItem <- alt6
                    #B PredItem alt6
                    alt6 = parse_string ("2")
                    #E PredItem alt6
                    #E BranchingItem -> alt6
                    seq3 = seq3 or alt6
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt7 = declare (False)
                    #B BranchingItem <- alt7
                    #B PredItem alt7
                    alt7 = parse_string ("3")
                    #E PredItem alt7
                    #E BranchingItem -> alt7
                    seq3 = seq3 or alt7
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt8 = declare (False)
                    #B BranchingItem <- alt8
                    #B PredItem alt8
                    alt8 = parse_string ("4")
                    #E PredItem alt8
                    #E BranchingItem -> alt8
                    seq3 = seq3 or alt8
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt9 = declare (False)
                    #B BranchingItem <- alt9
                    #B PredItem alt9
                    alt9 = parse_string ("5")
                    #E PredItem alt9
                    #E BranchingItem -> alt9
                    seq3 = seq3 or alt9
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt10 = declare (False)
                    #B BranchingItem <- alt10
                    #B PredItem alt10
                    alt10 = parse_string ("6")
                    #E PredItem alt10
                    #E BranchingItem -> alt10
                    seq3 = seq3 or alt10
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt11 = declare (False)
                    #B BranchingItem <- alt11
                    #B PredItem alt11
                    alt11 = parse_string ("7")
                    #E PredItem alt11
                    #E BranchingItem -> alt11
                    seq3 = seq3 or alt11
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt12 = declare (False)
                    #B BranchingItem <- alt12
                    #B PredItem alt12
                    alt12 = parse_string ("8")
                    #E PredItem alt12
                    #E BranchingItem -> alt12
                    seq3 = seq3 or alt12
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt13 = declare (False)
                    #B BranchingItem <- alt13
                    #B PredItem alt13
                    alt13 = parse_string ("9")
                    #E PredItem alt13
                    #E BranchingItem -> alt13
                    seq3 = seq3 or alt13
                #E AltItem -> seq3
                seqalt2 = seqalt2 or seq3
            while seq3:
                #B AltItem <- seq3
                if not seq3:
                    alt14 = declare (False)
                    #B BranchingItem <- alt14
                    #B PredItem alt14
                    alt14 = parse_string ("0")
                    #E PredItem alt14
                    #E BranchingItem -> alt14
                    seq3 = seq3 or alt14
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt15 = declare (False)
                    #B BranchingItem <- alt15
                    #B PredItem alt15
                    alt15 = parse_string ("1")
                    #E PredItem alt15
                    #E BranchingItem -> alt15
                    seq3 = seq3 or alt15
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt16 = declare (False)
                    #B BranchingItem <- alt16
                    #B PredItem alt16
                    alt16 = parse_string ("2")
                    #E PredItem alt16
                    #E BranchingItem -> alt16
                    seq3 = seq3 or alt16
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt17 = declare (False)
                    #B BranchingItem <- alt17
                    #B PredItem alt17
                    alt17 = parse_string ("3")
                    #E PredItem alt17
                    #E BranchingItem -> alt17
                    seq3 = seq3 or alt17
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt18 = declare (False)
                    #B BranchingItem <- alt18
                    #B PredItem alt18
                    alt18 = parse_string ("4")
                    #E PredItem alt18
                    #E BranchingItem -> alt18
                    seq3 = seq3 or alt18
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt19 = declare (False)
                    #B BranchingItem <- alt19
                    #B PredItem alt19
                    alt19 = parse_string ("5")
                    #E PredItem alt19
                    #E BranchingItem -> alt19
                    seq3 = seq3 or alt19
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt20 = declare (False)
                    #B BranchingItem <- alt20
                    #B PredItem alt20
                    alt20 = parse_string ("6")
                    #E PredItem alt20
                    #E BranchingItem -> alt20
                    seq3 = seq3 or alt20
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt21 = declare (False)
                    #B BranchingItem <- alt21
                    #B PredItem alt21
                    alt21 = parse_string ("7")
                    #E PredItem alt21
                    #E BranchingItem -> alt21
                    seq3 = seq3 or alt21
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt22 = declare (False)
                    #B BranchingItem <- alt22
                    #B PredItem alt22
                    alt22 = parse_string ("8")
                    #E PredItem alt22
                    #E BranchingItem -> alt22
                    seq3 = seq3 or alt22
                #E AltItem -> seq3
                #B AltItem <- seq3
                if not seq3:
                    alt23 = declare (False)
                    #B BranchingItem <- alt23
                    #B PredItem alt23
                    alt23 = parse_string ("9")
                    #E PredItem alt23
                    #E BranchingItem -> alt23
                    seq3 = seq3 or alt23
                #E AltItem -> seq3
            #E AltItem_pplus -> seqalt2
            seq1 = seq1 and seqalt2
            seqalt2 = declare (False)
        #E SeqItem_AlternationGroup -> seq1
        r = r and seq1
    if r:
        return accept ("number")
    else:
        return fail ("number")
