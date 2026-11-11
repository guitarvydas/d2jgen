
from plib2 import *
def main ():
    begin ("main")
    r = True
    # Sequence
    seq1=True
    if seq1:
        # SeqItem
        if seq1:
            # Alt Begin
            alt2 = False
            # Alt Clause
            alt3 = False
            if not alt2:
                # Sequence
                seq4=True
                if seq4:
                    # SeqItem
                    if seq4:
                        iplain5 = True
                        if  iplain5:
                            iplain5 =   a ()
                            
                        seq4 = seq4 and iplain5
                        
                    
                alt3 = alt3 and seq4
                
            alt2 = alt2 or alt3
            # Alt Clause
            alt6 = False
            if not alt2:
                # Sequence
                seq7=True
                if seq7:
                    # SeqItem
                    if seq7:
                        iplain8 = True
                        if  iplain8:
                            iplain8 =   b ()
                            
                        seq7 = seq7 and iplain8
                        
                    
                alt6 = alt6 and seq7
                
            alt2 = alt2 or alt6
            
        # SeqItem
        if seq1:
            iplain9 = True
            if  iplain9:
                iplain9 =   c ()
                
            seq1 = seq1 and iplain9
            
        
    r = r and seq1
    if r:
        return accept ("main")
    else:
        return fail ("main")
    
def a ():
    begin ("a")
    r = True
    # Sequence
    seq1=True
    if seq1:
        # SeqItem
        if seq1:
            iplain2 = True
            if  iplain2:
                iplain2 =  parse_string ("a")
                
            seq1 = seq1 and iplain2
            
        
    r = r and seq1
    if r:
        return accept ("a")
    else:
        return fail ("a")
    
def b ():
    begin ("b")
    r = True
    # Sequence
    seq1=True
    if seq1:
        # SeqItem
        if seq1:
            iplain2 = True
            if  iplain2:
                iplain2 =  parse_string ("b")
                
            seq1 = seq1 and iplain2
            
        
    r = r and seq1
    if r:
        return accept ("b")
    else:
        return fail ("b")
    
def c ():
    begin ("c")
    r = True
    # Sequence
    seq1=True
    if seq1:
        # SeqItem
        if seq1:
            iplain2 = True
            if  iplain2:
                iplain2 =  parse_string ("c")
                
            seq1 = seq1 and iplain2
            
        
    r = r and seq1
    if r:
        return accept ("c")
    else:
        return fail ("c")
    

