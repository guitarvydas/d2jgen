from plib2 import *
rulename = []
retvar = []
prevretvar = []
more = []
logicalop = []

def push (stack, v):
    stack.append (v)

def pop (stack):
    return stack.pop ()

def top (stack):
    return stack [-1]

def Rule ():
    global rulename, retvar, prevretvar, more, logicalop
    # Rule
    begin ("Rule")
    r = True
    # Sequence Begin
    seq1 = True
    # Alt Begin
    alt1 = False
    if not alt1:
        # Alt Unit 1
        alt2 = False
        if not alt2:
            # Sequence Unit 1
            seq3 = True
            if seq3:
                # Pred Unit 1
                seq3 = a ()
            print (f'A alt2={alt2} seq3={seq3}')
            alt2 = alt2 or seq3
            print (f'B alt2={alt2}')
            # end Sequence Unit
        alt1 = alt1 or alt2
    print (f'C alt1={alt1} not alt1={not alt1}')
    # end Alt Unit 1
    if not alt1:
        # Alt Unit 2
        alt4 = False
        if not alt4:
            # Sequence Unit 2
            seq = True
            if seq3:
                # Pred Unit 2
                seq3 = b ()
            alt1 = alt1 and seq3
            # end Sequence Unit 2
        alt1 = alt1 and alt4
        # end Alt Unit 2
    seq1 = seq1 or alt1
    # end Alt Begin
    if seq1:
        # Sequence Unit 3
        seq5 = True
        if seq5:
            # Pred Unit 3
            seq5 = c ()
            seq1 = seq1 and seq5
        # end Sequence Unit 3
    r = seq1
    # end Sequence Begin
    if r:
        return accept ("Rule")
    else:
        return fail ("Rule")

def a ():
    global rulename, retvar, prevretvar, more, logicalop
    # a
    r = True
    # Sequence Begin
    seq1 = True
    # Sequence Unit
    seq2 = True
    if seq2:
        # Pred Unit
        seq2 = parse_string ("a")
    seq1 = seq1 and seq2
    # end Sequence Begin
    r = seq1
    if r:
        return accept ("a")
    else:
        return fail ("a")
    # end "a"
    
def a ():
    global rulename, retvar, prevretvar, more, logicalop
    # a
    begin ("a")
    r = True
    # Sequence Begin
    seq1 = True
    # Sequence Unit
    seq2 = True
    if seq2:
        # Pred Unit
        seq2 = parse_string ("a")
    seq1 = seq1 and seq2
    # end Sequence Begin
    r = seq1
    if r:
        return accept ("a")
    else:
        return fail ("a")
    # end "a"


def b ():
    global rulename, retvar, prevretvar, more, logicalop
    # b
    begin ("b")
    r = True
    # Sequence Begin
    seq1 = True
    # Sequence Unit
    seq2 = True
    if seq2:
        # Pred Unit
        seq2 = parse_string ("b")
    seq1 = seq1 and seq2
    # end Sequence Begin
    r = seq1
    if r:
        return accept ("b")
    else:
        return fail ("b")
    # end "b"
    

def b ():
    global rulename, retvar, prevretvar, more, logicalop
    # b
    begin ("b")
    r = True
    # Sequence Begin
    seq1 = True
    # Sequence Unit
    seq2 = True
    if seq2:
        # Pred Unit
        seq2 = parse_string ("b")
    seq1 = seq1 and seq2
    # end Sequence Begin
    r = seq1
    if r:
        return accept ("b")
    else:
        return fail ("b")
    # end "b"
    

def c ():
    global rulename, retvar, prevretvar, more, logicalop
    # c
    begin ("c")
    r = True
    # Sequence Begin
    seq1 = True
    # Sequence Unit
    seq2 = True
    if seq2:
        # Pred Unit
        seq2 = parse_string ("c")
    seq1 = seq1 and seq2
    # end Sequence Begin
    r = seq1
    if r:
        return accept ("c")
    else:
        return fail ("c")
    # end "c"
    
