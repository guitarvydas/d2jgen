
from plib2 import *
def main ():
    begin ("main")
    r = True
    seq1=True
    if seq1:
        iplain2 = True
        if  iplain2:
            iplain2 =  parse_string ("a")
            
        seq1 = seq1 and iplain2
        
    r = r and seq1
    if r:
        return accept ("main")
    else:
        return fail ("main")
    

