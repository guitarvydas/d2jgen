
from plib2 import *
def main ():
    begin ("main")
    toplex1 = True
    alt2 = False
    if not alt2:
        seqi3 = True
        iplain4 =   a ()
        seqi3 = seqi3 and iplain4
        alt2 = alt2 and seqi3
        
    toplex1 = toplex1 or alt2
    seqi5 = True
    iplain6 =   b ()
    seqi5 = seqi5 and iplain6
    toplex1 = toplex1 and seqi5
    if toplex1:
        return accept ("main")
    else:
        return fail ("main")
def a ():
    begin ("a")
    toplex1 = True
    seqi2 = True
    iplain3 =  parse_string ("a")
    seqi2 = seqi2 and iplain3
    toplex1 = toplex1 and seqi2
    if toplex1:
        return accept ("a")
    else:
        return fail ("a")
def b ():
    begin ("b")
    toplex1 = True
    seqi2 = True
    iplain3 =  parse_string ("b")
    seqi2 = seqi2 and iplain3
    toplex1 = toplex1 and seqi2
    if toplex1:
        return accept ("b")
    else:
        return fail ("b")

