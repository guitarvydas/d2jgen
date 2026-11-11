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
    push (rulename, "Rule")                                          #meta
    push (retvar, "r")                                               #meta
    r = True
    # Sequence Begin
    push (prevretvar, top (retvar))                                  #meta
    push (retvar, "seq1")                                            #meta
    seq1 = True
    push (more, "")                                                  #meta
    push (logicalop, "and")                                          #meta
    # Alt Begin
    push (prevretvar, top (retvar))                                  #meta
    push (retvar, "alt1")                                            #meta
    alt1 = False
    push (more, "not")                                               #meta
    push (logicalop, "or")                                           #meta
    if not alt1:
        # Alt Unit 1
        push (prevretvar, top (retvar))                                  #meta
        push (retvar, "alt2")                                            #meta
        alt2 = False
        if not alt2:
            # Sequence Unit 1
            push (prevretvar, "alt2")                                    #meta
            push (retvar, "seq3")                                        #meta
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
        push (prevretvar, "alt1")                                        #meta
        push (retvar, "alt4")                                            #meta
        alt4 = False
        if not alt4:
            # Sequence Unit 2
            push (prevretvar, "alt4")                                    #meta
            push (retvar, "seq3")                                        #meta
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
        push (prevretvar, "seq1")                                    #meta
        push (retvar, "seq5")                                        #meta
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
    push (rulename, "a")                                          #meta
    push (retvar, "r")                                               #meta
    r = True
    # Sequence Begin
    push (prevretvar, top (retvar))                                  #meta
    push (retvar, "seq1")                                            #meta
    seq1 = True
    push (more, "")                                                  #meta
    push (logicalop, "and")                                          #meta
    # Sequence Unit
    push (prevretvar, "r")                                        #meta
    push (retvar, "seq2")                                            #meta
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
    push (rulename, "a")                                          #meta
    push (retvar, "r")                                               #meta
    r = True
    # Sequence Begin
    push (prevretvar, top (retvar))                                  #meta
    push (retvar, "seq1")                                            #meta
    seq1 = True
    push (more, "")                                                  #meta
    push (logicalop, "and")                                          #meta
    # Sequence Unit
    push (prevretvar, "r")                                        #meta
    push (retvar, "seq2")                                            #meta
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
    push (rulename, "b")                                          #meta
    push (retvar, "r")                                               #meta
    r = True
    # Sequence Begin
    push (prevretvar, top (retvar))                                  #meta
    push (retvar, "seq1")                                            #meta
    seq1 = True
    push (more, "")                                                  #meta
    push (logicalop, "and")                                          #meta
    # Sequence Unit
    push (prevretvar, "r")                                        #meta
    push (retvar, "seq2")                                            #meta
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
    push (rulename, "b")                                          #meta
    push (retvar, "r")                                               #meta
    r = True
    # Sequence Begin
    push (prevretvar, top (retvar))                                  #meta
    push (retvar, "seq1")                                            #meta
    seq1 = True
    push (more, "")                                                  #meta
    push (logicalop, "and")                                          #meta
    # Sequence Unit
    push (prevretvar, "r")                                        #meta
    push (retvar, "seq2")                                            #meta
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
    push (rulename, "c")                                          #meta
    push (retvar, "r")                                               #meta
    r = True
    # Sequence Begin
    push (prevretvar, top (retvar))                                  #meta
    push (retvar, "seq1")                                            #meta
    seq1 = True
    push (more, "")                                                  #meta
    push (logicalop, "and")                                          #meta
    # Sequence Unit
    push (prevretvar, "r")                                        #meta
    push (retvar, "seq2")                                            #meta
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
    
