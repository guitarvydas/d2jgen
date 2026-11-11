
from plib2 import *
def main ():
    begin ("main")
    toplex1 = True
    seq3=True
    if seq3:
        iplain4 =   a ()
        seq3 = seq3 and iplain4
        
    seq5=True
    if seq5:
        iplain6 =   b ()
        seq5 = seq5 and iplain6
        
    seq7=True
    if seq7:
        iplain8 =   b ()
        seq7 = seq7 and iplain8
        
    if toplex1:
        return accept ("main")
    else:
        return fail ("main")
    
def a ():
    begin ("a")
    toplex1 = True
    seq2=True
    if seq2:
        iplain3 =  parse_string ("a")
        seq2 = seq2 and iplain3
        
    if toplex1:
        return accept ("a")
    else:
        return fail ("a")
    
def b ():
    begin ("b")
    toplex1 = True
    seq2=True
    if seq2:
        iplain3 =  parse_string ("b")
        seq2 = seq2 and iplain3
        
    if toplex1:
        return accept ("b")
    else:
        return fail ("b")
    

