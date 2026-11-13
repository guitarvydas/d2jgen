from plib2 import *
def main ():
    begin ("main")
    r = True
    if r:
        seq1 =  a ()
        r = r and seq1
    if r:
        seq2 =  c ()
        r = r and seq2
    if r:
        return accept ("main")
    else:
        return fail ("main")
