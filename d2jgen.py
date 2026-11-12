from plib2 import *
def main ():
    begin ("main")
    r = True
    seq1 = True
    if  r:
        # BA_altplain
        seq2 = False
        if not seq1:
            seq3 = True
            if  seq2:
                seq3 =   x ()
            seq2 = seq2 and seq3
            seq1 = seq1 or  seq2
        if not seq1:
            seq4 = True
            if  seq2:
                seq4 =   y ()
            seq2 = seq2 and seq4
            seq1 = seq1 or  seq2
    r = r and seq1
    if r:
        return accept ("main")
    else:
        return fail ("main")
