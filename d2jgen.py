
from plib2 import *
def main ():
    begin ("main")
    toplex1 = True
    # alt plain 1
    # alt first 1
    alt2 = False
    # alt first 2
    if not alt2:
        # alt first 3
        # seqi 1
        seqi3 = True
        # seqi 2
        iplain4 =   a ()
        seqi3 = seqi3 and iplain4
        # seqi 3
        alt2 = alt2 and seqi3
        # seqi fini
        
    # alt first end
    # alt plain 2
    # alt last 1
    if not alt2:
        # alt last 2
        # seqi 1
        seqi5 = True
        # seqi 2
        iplain6 =   b ()
        seqi5 = seqi5 and iplain6
        # seqi 3
        alt2 = alt2 and seqi5
        # seqi fini
        
    # alt last end
    # alt plain ending
    toplex1 = toplex1 or alt2
    # alt plain end
    # seqi 1
    seqi7 = True
    # seqi 2
    iplain8 =   b ()
    seqi7 = seqi7 and iplain8
    # seqi 3
    toplex1 = toplex1 and seqi7
    # seqi fini
    if toplex1:
        return accept ("main")
    else:
        return fail ("main")
def a ():
    begin ("a")
    toplex1 = True
    # seqi 1
    seqi2 = True
    # seqi 2
    iplain3 =  parse_string ("a")
    seqi2 = seqi2 and iplain3
    # seqi 3
    toplex1 = toplex1 and seqi2
    # seqi fini
    if toplex1:
        return accept ("a")
    else:
        return fail ("a")
def b ():
    begin ("b")
    toplex1 = True
    # seqi 1
    seqi2 = True
    # seqi 2
    iplain3 =  parse_string ("b")
    seqi2 = seqi2 and iplain3
    # seqi 3
    toplex1 = toplex1 and seqi2
    # seqi fini
    if toplex1:
        return accept ("b")
    else:
        return fail ("b")

