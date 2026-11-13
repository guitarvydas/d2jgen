from plib2 import *
def main ():
    begin ("main")
    r = True
    if r:
        seq1 = True
        # begin SeqItem_alternation
        # begin Alternation_parenthesized
        # begin AltItem
        |
        # begin BranchingItem
        if seq1:
            seq2 = True
            # end SeqItem_preditem
            if seq2:
                seq3 = True
                # begin end PredItem
                seq3 =  a ()
                # end PredItem
                seq2 = seq2 and seq3
            # end SeqItem_preditem
            seq1 = seq1 and seq2
        # end BranchingItem
        # end AltItem
        # begin AltItem
        |
        # begin BranchingItem
        if seq1:
            seq4 = True
            # end SeqItem_preditem
            if seq4:
                seq5 = True
                # begin end PredItem
                seq5 =  b ()
                # end PredItem
                seq4 = seq4 and seq5
            # end SeqItem_preditem
            seq1 = seq1 and seq4
        # end BranchingItem
        # end AltItem
        # end Alternation_parenthesized
        # end SeqItem_alternation
        # end SeqItem_preditem
        if seq1:
            seq6 = True
            # begin end PredItem
            seq6 =  c ()
            # end PredItem
            seq1 = seq1 and seq6
        # end SeqItem_preditem
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
        # end SeqItem_preditem
        if seq1:
            seq2 = True
            # begin end PredItem
            seq2 = parse_string ("a")
            # end PredItem
            seq1 = seq1 and seq2
        # end SeqItem_preditem
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
        # end SeqItem_preditem
        if seq1:
            seq2 = True
            # begin end PredItem
            seq2 = parse_string ("b")
            # end PredItem
            seq1 = seq1 and seq2
        # end SeqItem_preditem
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
        # end SeqItem_preditem
        if seq1:
            seq2 = True
            # begin end PredItem
            seq2 = parse_string ("c")
            # end PredItem
            seq1 = seq1 and seq2
        # end SeqItem_preditem
        r = r and seq1
    if r:
        return accept ("c")
    else:
        return fail ("c")
