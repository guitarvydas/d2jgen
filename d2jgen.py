from plib2 import *
def main ():
    begin ("main")
    r = True
    if r:
        seq1 = True
        # begin SeqItem_alternation
        # begin AltItem_parenthesized
        if seq1:
            seq2 = False
            # begin AltItem
            if not seq2:
                seq3 = False
                # begin BranchingItem
                if seq3:
                    seq4 = True
                    # begin SeqItem_preditem
                    if seq4:
                        seq4 = a ()
                    # end SeqItem_preditem
                    seq3 = seq3 and seq4
                # end BranchingItem
            seq2 = seq2 or seq3
            # end AltItem
            # begin AltItem
            if not seq2:
                seq6 = False
                # begin BranchingItem
                if seq6:
                    seq7 = True
                    # begin SeqItem_preditem
                    if seq7:
                        seq7 = b ()
                    # end SeqItem_preditem
                    seq6 = seq6 and seq7
                # end BranchingItem
            seq2 = seq2 or seq6
            # end AltItem
        seq1 = seq1 or seq2
        # end AltItem_parenthesized
        # end SeqItem_alternation
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
        # begin SeqItem_preditem
        if seq1:
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
        # begin SeqItem_preditem
        if seq1:
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
        # begin SeqItem_preditem
        if seq1:
            seq2 = parse_string ("c")
            # end PredItem
            seq1 = seq1 and seq2
        # end SeqItem_preditem
        r = r and seq1
    if r:
        return accept ("c")
    else:
        return fail ("c")
