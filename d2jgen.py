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
                v7 = parse_ignoring (lambda :  b ())
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
                v9 = parse_ignoring (lambda :  a ())
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
                    v11 = parse_ignoring (lambda :  b ())
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
                    v13 = parse_ignoring (lambda :  a ())
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
    v2 = v3
    bp_syn1 = v3
    ###                            <<out Group bypass=bp_syn1 target=v2
    if v2:
        return accept ("Main")
    else:
        return fail ("Main")
    ###                                 <<out RuleBody
def a ():
    ###                                 >>in RuleBody
    begin ("a")
    bp_lex1=declare(False)
    v2=declare(False)
    ###                             >>in Group bypass=bp_lex1 target=v2
    bp_4 = declare (False)
    v3 = declare (None)
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = parse_string ("a")
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    v2 = v3
    bp_lex1 = v3
    ###                            <<out Group bypass=bp_lex1 target=v2
    if v2:
        return accept ("a")
    else:
        return fail ("a")
    ###                                 <<out RuleBody
def b ():
    ###                                 >>in RuleBody
    begin ("b")
    bp_lex1=declare(False)
    v2=declare(False)
    ###                             >>in Group bypass=bp_lex1 target=v2
    bp_4 = declare (False)
    v3 = declare (None)
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = parse_string ("b")
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    v2 = v3
    bp_lex1 = v3
    ###                            <<out Group bypass=bp_lex1 target=v2
    if v2:
        return accept ("b")
    else:
        return fail ("b")
    ###                                 <<out RuleBody
