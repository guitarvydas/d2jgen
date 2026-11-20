from plib2 import *
import sys
def Main ():
    ###                                 >>in RuleBody
    begin ("Main")
    bp_syn1=declare(False)
    v2=declare(False)
    ###                             >>in Group bypass=bp_syn1 target=v2
    bp_4 = declare (False)
    v3 = declare (None)
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = parse_ignoring (lambda :  Array ())
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    v2 = v3
    bp_syn1 = v3
    ###                            <<out Group bypass=bp_syn1 target=v2
    if v2:
        return accept ("Main")
    else:
        return fail ("Main")
    ###                                 <<out RuleBody
def Array ():
    ###                                 >>in RuleBody
    begin ("Array")
    bp_syn1=declare(False)
    v2=declare(False)
    ###                             >>in Group bypass=bp_syn1 target=v2
    bp_4 = declare (False)
    v3 = declare (None)
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = parse_ignoring (lambda : parse_string ("["))
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in altgroupPLUS bypass=bp_4 target=v3
        bp_6 = declare (False)
        v5 = declare (None)
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_8 = declare (False)
            v7 = declare (None)
            ###                             >>in SequentialItem bypass=bp_8 target=v7
            if not bp_8:
                ###                             >>in Pred target=v7
                v7 = parse_ignoring (lambda :  KV ())
                ###                             <<out Pred target=v7
                bp_8 = not v7 ##anding
            ###                             <<out SequentialItem bypass=bp_8 target=v7
            v5 = v7
            bp_6 = v7
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_10 = declare (False)
            v9 = declare (None)
            ###                             >>in SequentialItem bypass=bp_10 target=v9
            if not bp_10:
                ###                             >>in Pred target=v9
                v9 = parse_ignoring (lambda :  Object ())
                ###                             <<out Pred target=v9
                bp_10 = not v9 ##anding
            ###                             <<out SequentialItem bypass=bp_10 target=v9
            v5 = v9
            bp_6 = v9
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        v3 = v5
        bp_4 = bp_6
        ###                             >>in PLUS bypass=bp_4 target=v3
        while v5:
            bp_6 = False
            ###                             >>in AltItem bypass=bp_6 target=v5
            if not bp_6:
                ###                             >>in Group bypass=bp_6 target=v5
                bp_12 = declare (False)
                v11 = declare (None)
                ###                             >>in SequentialItem bypass=bp_12 target=v11
                if not bp_12:
                    ###                             >>in Pred target=v11
                    v11 = parse_ignoring (lambda :  KV ())
                    ###                             <<out Pred target=v11
                    bp_12 = not v11 ##anding
                ###                             <<out SequentialItem bypass=bp_12 target=v11
                v5 = v11
                bp_6 = v11
                ###                            <<out Group bypass=bp_6 target=v5
                bp_6 = v5##oring
            ###                             <<out AltItem bypass=bp_6 target=v5
            ###                             >>in AltItem bypass=bp_6 target=v5
            if not bp_6:
                ###                             >>in Group bypass=bp_6 target=v5
                bp_14 = declare (False)
                v13 = declare (None)
                ###                             >>in SequentialItem bypass=bp_14 target=v13
                if not bp_14:
                    ###                             >>in Pred target=v13
                    v13 = parse_ignoring (lambda :  Object ())
                    ###                             <<out Pred target=v13
                    bp_14 = not v13 ##anding
                ###                             <<out SequentialItem bypass=bp_14 target=v13
                v5 = v13
                bp_6 = v13
                ###                            <<out Group bypass=bp_6 target=v5
                bp_6 = v5##oring
            ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             <<out PLUS bypass=bp_4 target=v3
        ###                             <<out altgroupPLUS savedbypass=bp_4 savedtarget=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = parse_ignoring (lambda : parse_string ("]"))
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    v2 = v3
    bp_syn1 = v3
    ###                            <<out Group bypass=bp_syn1 target=v2
    if v2:
        return accept ("Array")
    else:
        return fail ("Array")
    ###                                 <<out RuleBody
def Object ():
    ###                                 >>in RuleBody
    begin ("Object")
    bp_syn1=declare(False)
    v2=declare(False)
    ###                             >>in Group bypass=bp_syn1 target=v2
    bp_4 = declare (False)
    v3 = declare (None)
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = parse_ignoring (lambda : parse_string ("{"))
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = parse_ignoring (lambda :  KV ())
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    while v3:
        bp_4 = False
        ###                             >>in Pred target=v3
        v3 = parse_ignoring (lambda :  KV ())
        ###                             <<out Pred target=v3
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = parse_ignoring (lambda : parse_string ("}"))
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    v2 = v3
    bp_syn1 = v3
    ###                            <<out Group bypass=bp_syn1 target=v2
    if v2:
        return accept ("Object")
    else:
        return fail ("Object")
    ###                                 <<out RuleBody
def KV ():
    ###                                 >>in RuleBody
    begin ("KV")
    bp_syn1=declare(False)
    v2=declare(False)
    ###                             >>in Group bypass=bp_syn1 target=v2
    bp_4 = declare (False)
    v3 = declare (None)
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = parse_ignoring (lambda :  keystring ())
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = parse_ignoring (lambda : parse_string (":"))
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in altgroup bypass=bp_4 target=v3
        bp_6 = declare (False)
        v5 = declare (None)
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_8 = declare (False)
            v7 = declare (None)
            ###                             >>in SequentialItem bypass=bp_8 target=v7
            if not bp_8:
                ###                             >>in Pred target=v7
                v7 = parse_ignoring (lambda :  Array ())
                ###                             <<out Pred target=v7
                bp_8 = not v7 ##anding
            ###                             <<out SequentialItem bypass=bp_8 target=v7
            v5 = v7
            bp_6 = v7
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_10 = declare (False)
            v9 = declare (None)
            ###                             >>in SequentialItem bypass=bp_10 target=v9
            if not bp_10:
                ###                             >>in Pred target=v9
                v9 = parse_ignoring (lambda :  Object ())
                ###                             <<out Pred target=v9
                bp_10 = not v9 ##anding
            ###                             <<out SequentialItem bypass=bp_10 target=v9
            v5 = v9
            bp_6 = v9
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_12 = declare (False)
            v11 = declare (None)
            ###                             >>in SequentialItem bypass=bp_12 target=v11
            if not bp_12:
                ###                             >>in Pred target=v11
                v11 = parse_ignoring (lambda :  string ())
                ###                             <<out Pred target=v11
                bp_12 = not v11 ##anding
            ###                             <<out SequentialItem bypass=bp_12 target=v11
            v5 = v11
            bp_6 = v11
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_14 = declare (False)
            v13 = declare (None)
            ###                             >>in SequentialItem bypass=bp_14 target=v13
            if not bp_14:
                ###                             >>in Pred target=v13
                v13 = parse_ignoring (lambda :  emptyString ())
                ###                             <<out Pred target=v13
                bp_14 = not v13 ##anding
            ###                             <<out SequentialItem bypass=bp_14 target=v13
            v5 = v13
            bp_6 = v13
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_16 = declare (False)
            v15 = declare (None)
            ###                             >>in SequentialItem bypass=bp_16 target=v15
            if not bp_16:
                ###                             >>in Pred target=v15
                v15 = parse_ignoring (lambda :  number ())
                ###                             <<out Pred target=v15
                bp_16 = not v15 ##anding
            ###                             <<out SequentialItem bypass=bp_16 target=v15
            v5 = v15
            bp_6 = v15
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        v3 = v5
        bp_4 = bp_6
        ###                             <<out altgroup savedbypass=bp_4 savedtarget=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    v2 = v3
    bp_syn1 = v3
    ###                            <<out Group bypass=bp_syn1 target=v2
    if v2:
        return accept ("KV")
    else:
        return fail ("KV")
    ###                                 <<out RuleBody
def string ():
    ###                                 >>in RuleBody
    begin ("string")
    bp_lex1=declare(False)
    v2=declare(False)
    ###                             >>in Group bypass=bp_lex1 target=v2
    bp_4 = declare (False)
    v3 = declare (None)
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = parse_string ("\"")
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 =  strchar ()
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    while v3:
        bp_4 = False
        ###                             >>in Pred target=v3
        v3 =  strchar ()
        ###                             <<out Pred target=v3
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = parse_string ("\"")
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    v2 = v3
    bp_lex1 = v3
    ###                            <<out Group bypass=bp_lex1 target=v2
    if v2:
        return accept ("string")
    else:
        return fail ("string")
    ###                                 <<out RuleBody
def strchar ():
    ###                                 >>in RuleBody
    begin ("strchar")
    bp_lex1=declare(False)
    v2=declare(False)
    ###                             >>in Group bypass=bp_lex1 target=v2
    bp_4 = declare (False)
    v3 = declare (None)
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = not parse_string ("\"")
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 =  any ()
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    v2 = v3
    bp_lex1 = v3
    ###                            <<out Group bypass=bp_lex1 target=v2
    if v2:
        return accept ("strchar")
    else:
        return fail ("strchar")
    ###                                 <<out RuleBody
def keystring ():
    ###                                 >>in RuleBody
    begin ("keystring")
    bp_lex1=declare(False)
    v2=declare(False)
    ###                             >>in Group bypass=bp_lex1 target=v2
    bp_4 = declare (False)
    v3 = declare (None)
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 =  string ()
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    v2 = v3
    bp_lex1 = v3
    ###                            <<out Group bypass=bp_lex1 target=v2
    if v2:
        return accept ("keystring")
    else:
        return fail ("keystring")
    ###                                 <<out RuleBody
def emptyString ():
    ###                                 >>in RuleBody
    begin ("emptyString")
    bp_lex1=declare(False)
    v2=declare(False)
    ###                             >>in Group bypass=bp_lex1 target=v2
    bp_4 = declare (False)
    v3 = declare (None)
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = parse_string ("\"")
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = parse_string ("\"")
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    v2 = v3
    bp_lex1 = v3
    ###                            <<out Group bypass=bp_lex1 target=v2
    if v2:
        return accept ("emptyString")
    else:
        return fail ("emptyString")
    ###                                 <<out RuleBody
def number ():
    ###                                 >>in RuleBody
    begin ("number")
    bp_lex1=declare(False)
    v2=declare(False)
    ###                             >>in Group bypass=bp_lex1 target=v2
    bp_4 = declare (False)
    v3 = declare (None)
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in altgroupPLUS bypass=bp_4 target=v3
        bp_6 = declare (False)
        v5 = declare (None)
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_8 = declare (False)
            v7 = declare (None)
            ###                             >>in SequentialItem bypass=bp_8 target=v7
            if not bp_8:
                ###                             >>in Pred target=v7
                v7 = parse_string ("0")
                ###                             <<out Pred target=v7
                bp_8 = not v7 ##anding
            ###                             <<out SequentialItem bypass=bp_8 target=v7
            v5 = v7
            bp_6 = v7
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_10 = declare (False)
            v9 = declare (None)
            ###                             >>in SequentialItem bypass=bp_10 target=v9
            if not bp_10:
                ###                             >>in Pred target=v9
                v9 = parse_string ("1")
                ###                             <<out Pred target=v9
                bp_10 = not v9 ##anding
            ###                             <<out SequentialItem bypass=bp_10 target=v9
            v5 = v9
            bp_6 = v9
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_12 = declare (False)
            v11 = declare (None)
            ###                             >>in SequentialItem bypass=bp_12 target=v11
            if not bp_12:
                ###                             >>in Pred target=v11
                v11 = parse_string ("2")
                ###                             <<out Pred target=v11
                bp_12 = not v11 ##anding
            ###                             <<out SequentialItem bypass=bp_12 target=v11
            v5 = v11
            bp_6 = v11
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_14 = declare (False)
            v13 = declare (None)
            ###                             >>in SequentialItem bypass=bp_14 target=v13
            if not bp_14:
                ###                             >>in Pred target=v13
                v13 = parse_string ("3")
                ###                             <<out Pred target=v13
                bp_14 = not v13 ##anding
            ###                             <<out SequentialItem bypass=bp_14 target=v13
            v5 = v13
            bp_6 = v13
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_16 = declare (False)
            v15 = declare (None)
            ###                             >>in SequentialItem bypass=bp_16 target=v15
            if not bp_16:
                ###                             >>in Pred target=v15
                v15 = parse_string ("4")
                ###                             <<out Pred target=v15
                bp_16 = not v15 ##anding
            ###                             <<out SequentialItem bypass=bp_16 target=v15
            v5 = v15
            bp_6 = v15
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_18 = declare (False)
            v17 = declare (None)
            ###                             >>in SequentialItem bypass=bp_18 target=v17
            if not bp_18:
                ###                             >>in Pred target=v17
                v17 = parse_string ("5")
                ###                             <<out Pred target=v17
                bp_18 = not v17 ##anding
            ###                             <<out SequentialItem bypass=bp_18 target=v17
            v5 = v17
            bp_6 = v17
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_20 = declare (False)
            v19 = declare (None)
            ###                             >>in SequentialItem bypass=bp_20 target=v19
            if not bp_20:
                ###                             >>in Pred target=v19
                v19 = parse_string ("6")
                ###                             <<out Pred target=v19
                bp_20 = not v19 ##anding
            ###                             <<out SequentialItem bypass=bp_20 target=v19
            v5 = v19
            bp_6 = v19
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_22 = declare (False)
            v21 = declare (None)
            ###                             >>in SequentialItem bypass=bp_22 target=v21
            if not bp_22:
                ###                             >>in Pred target=v21
                v21 = parse_string ("7")
                ###                             <<out Pred target=v21
                bp_22 = not v21 ##anding
            ###                             <<out SequentialItem bypass=bp_22 target=v21
            v5 = v21
            bp_6 = v21
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_24 = declare (False)
            v23 = declare (None)
            ###                             >>in SequentialItem bypass=bp_24 target=v23
            if not bp_24:
                ###                             >>in Pred target=v23
                v23 = parse_string ("8")
                ###                             <<out Pred target=v23
                bp_24 = not v23 ##anding
            ###                             <<out SequentialItem bypass=bp_24 target=v23
            v5 = v23
            bp_6 = v23
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             >>in AltItem bypass=bp_6 target=v5
        if not bp_6:
            ###                             >>in Group bypass=bp_6 target=v5
            bp_26 = declare (False)
            v25 = declare (None)
            ###                             >>in SequentialItem bypass=bp_26 target=v25
            if not bp_26:
                ###                             >>in Pred target=v25
                v25 = parse_string ("9")
                ###                             <<out Pred target=v25
                bp_26 = not v25 ##anding
            ###                             <<out SequentialItem bypass=bp_26 target=v25
            v5 = v25
            bp_6 = v25
            ###                            <<out Group bypass=bp_6 target=v5
            bp_6 = v5##oring
        ###                             <<out AltItem bypass=bp_6 target=v5
        v3 = v5
        bp_4 = bp_6
        ###                             >>in PLUS bypass=bp_4 target=v3
        while v5:
            bp_6 = False
            ###                             >>in AltItem bypass=bp_6 target=v5
            if not bp_6:
                ###                             >>in Group bypass=bp_6 target=v5
                bp_28 = declare (False)
                v27 = declare (None)
                ###                             >>in SequentialItem bypass=bp_28 target=v27
                if not bp_28:
                    ###                             >>in Pred target=v27
                    v27 = parse_string ("0")
                    ###                             <<out Pred target=v27
                    bp_28 = not v27 ##anding
                ###                             <<out SequentialItem bypass=bp_28 target=v27
                v5 = v27
                bp_6 = v27
                ###                            <<out Group bypass=bp_6 target=v5
                bp_6 = v5##oring
            ###                             <<out AltItem bypass=bp_6 target=v5
            ###                             >>in AltItem bypass=bp_6 target=v5
            if not bp_6:
                ###                             >>in Group bypass=bp_6 target=v5
                bp_30 = declare (False)
                v29 = declare (None)
                ###                             >>in SequentialItem bypass=bp_30 target=v29
                if not bp_30:
                    ###                             >>in Pred target=v29
                    v29 = parse_string ("1")
                    ###                             <<out Pred target=v29
                    bp_30 = not v29 ##anding
                ###                             <<out SequentialItem bypass=bp_30 target=v29
                v5 = v29
                bp_6 = v29
                ###                            <<out Group bypass=bp_6 target=v5
                bp_6 = v5##oring
            ###                             <<out AltItem bypass=bp_6 target=v5
            ###                             >>in AltItem bypass=bp_6 target=v5
            if not bp_6:
                ###                             >>in Group bypass=bp_6 target=v5
                bp_32 = declare (False)
                v31 = declare (None)
                ###                             >>in SequentialItem bypass=bp_32 target=v31
                if not bp_32:
                    ###                             >>in Pred target=v31
                    v31 = parse_string ("2")
                    ###                             <<out Pred target=v31
                    bp_32 = not v31 ##anding
                ###                             <<out SequentialItem bypass=bp_32 target=v31
                v5 = v31
                bp_6 = v31
                ###                            <<out Group bypass=bp_6 target=v5
                bp_6 = v5##oring
            ###                             <<out AltItem bypass=bp_6 target=v5
            ###                             >>in AltItem bypass=bp_6 target=v5
            if not bp_6:
                ###                             >>in Group bypass=bp_6 target=v5
                bp_34 = declare (False)
                v33 = declare (None)
                ###                             >>in SequentialItem bypass=bp_34 target=v33
                if not bp_34:
                    ###                             >>in Pred target=v33
                    v33 = parse_string ("3")
                    ###                             <<out Pred target=v33
                    bp_34 = not v33 ##anding
                ###                             <<out SequentialItem bypass=bp_34 target=v33
                v5 = v33
                bp_6 = v33
                ###                            <<out Group bypass=bp_6 target=v5
                bp_6 = v5##oring
            ###                             <<out AltItem bypass=bp_6 target=v5
            ###                             >>in AltItem bypass=bp_6 target=v5
            if not bp_6:
                ###                             >>in Group bypass=bp_6 target=v5
                bp_36 = declare (False)
                v35 = declare (None)
                ###                             >>in SequentialItem bypass=bp_36 target=v35
                if not bp_36:
                    ###                             >>in Pred target=v35
                    v35 = parse_string ("4")
                    ###                             <<out Pred target=v35
                    bp_36 = not v35 ##anding
                ###                             <<out SequentialItem bypass=bp_36 target=v35
                v5 = v35
                bp_6 = v35
                ###                            <<out Group bypass=bp_6 target=v5
                bp_6 = v5##oring
            ###                             <<out AltItem bypass=bp_6 target=v5
            ###                             >>in AltItem bypass=bp_6 target=v5
            if not bp_6:
                ###                             >>in Group bypass=bp_6 target=v5
                bp_38 = declare (False)
                v37 = declare (None)
                ###                             >>in SequentialItem bypass=bp_38 target=v37
                if not bp_38:
                    ###                             >>in Pred target=v37
                    v37 = parse_string ("5")
                    ###                             <<out Pred target=v37
                    bp_38 = not v37 ##anding
                ###                             <<out SequentialItem bypass=bp_38 target=v37
                v5 = v37
                bp_6 = v37
                ###                            <<out Group bypass=bp_6 target=v5
                bp_6 = v5##oring
            ###                             <<out AltItem bypass=bp_6 target=v5
            ###                             >>in AltItem bypass=bp_6 target=v5
            if not bp_6:
                ###                             >>in Group bypass=bp_6 target=v5
                bp_40 = declare (False)
                v39 = declare (None)
                ###                             >>in SequentialItem bypass=bp_40 target=v39
                if not bp_40:
                    ###                             >>in Pred target=v39
                    v39 = parse_string ("6")
                    ###                             <<out Pred target=v39
                    bp_40 = not v39 ##anding
                ###                             <<out SequentialItem bypass=bp_40 target=v39
                v5 = v39
                bp_6 = v39
                ###                            <<out Group bypass=bp_6 target=v5
                bp_6 = v5##oring
            ###                             <<out AltItem bypass=bp_6 target=v5
            ###                             >>in AltItem bypass=bp_6 target=v5
            if not bp_6:
                ###                             >>in Group bypass=bp_6 target=v5
                bp_42 = declare (False)
                v41 = declare (None)
                ###                             >>in SequentialItem bypass=bp_42 target=v41
                if not bp_42:
                    ###                             >>in Pred target=v41
                    v41 = parse_string ("7")
                    ###                             <<out Pred target=v41
                    bp_42 = not v41 ##anding
                ###                             <<out SequentialItem bypass=bp_42 target=v41
                v5 = v41
                bp_6 = v41
                ###                            <<out Group bypass=bp_6 target=v5
                bp_6 = v5##oring
            ###                             <<out AltItem bypass=bp_6 target=v5
            ###                             >>in AltItem bypass=bp_6 target=v5
            if not bp_6:
                ###                             >>in Group bypass=bp_6 target=v5
                bp_44 = declare (False)
                v43 = declare (None)
                ###                             >>in SequentialItem bypass=bp_44 target=v43
                if not bp_44:
                    ###                             >>in Pred target=v43
                    v43 = parse_string ("8")
                    ###                             <<out Pred target=v43
                    bp_44 = not v43 ##anding
                ###                             <<out SequentialItem bypass=bp_44 target=v43
                v5 = v43
                bp_6 = v43
                ###                            <<out Group bypass=bp_6 target=v5
                bp_6 = v5##oring
            ###                             <<out AltItem bypass=bp_6 target=v5
            ###                             >>in AltItem bypass=bp_6 target=v5
            if not bp_6:
                ###                             >>in Group bypass=bp_6 target=v5
                bp_46 = declare (False)
                v45 = declare (None)
                ###                             >>in SequentialItem bypass=bp_46 target=v45
                if not bp_46:
                    ###                             >>in Pred target=v45
                    v45 = parse_string ("9")
                    ###                             <<out Pred target=v45
                    bp_46 = not v45 ##anding
                ###                             <<out SequentialItem bypass=bp_46 target=v45
                v5 = v45
                bp_6 = v45
                ###                            <<out Group bypass=bp_6 target=v5
                bp_6 = v5##oring
            ###                             <<out AltItem bypass=bp_6 target=v5
        ###                             <<out PLUS bypass=bp_4 target=v3
        ###                             <<out altgroupPLUS savedbypass=bp_4 savedtarget=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    v2 = v3
    bp_lex1 = v3
    ###                            <<out Group bypass=bp_lex1 target=v2
    if v2:
        return accept ("number")
    else:
        return fail ("number")
    ###                                 <<out RuleBody
