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
        v3 = parse_ignoring (lambda : parse_string ("{"))
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    ###                             <<out SequentialItem bypass=bp_4 target=v3
    ###                             >>in SequentialItem bypass=bp_4 target=v3
    if not bp_4:
        ###                             >>in Pred target=v3
        v3 = parse_ignoring (lambda :  a ())
        ###                             <<out Pred target=v3
        bp_4 = not v3 ##anding
    while v3:
        bp_4 = False
        ###                             >>in Pred target=v3
        v3 = parse_ignoring (lambda :  a ())
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
