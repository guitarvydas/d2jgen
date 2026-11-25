from plib2 import *
import sys
def Main ():
    begin ("Main")
    bp_syn1=declare(False)
    v2=declare(False)
    bp_4 = declare (False)
    v3 = declare (None)
    if not bp_4:
        v3 = parse_ignoring (lambda :  Array ())
        bp_4 = not v3
    v2 = v3
    bp_syn1 = v3
    if v2:
        return accept ("Main")
    else:
        return fail ("Main")
def Array ():
    begin ("Array")
    bp_syn1=declare(False)
    v2=declare(False)
    bp_4 = declare (False)
    v3 = declare (None)
    if not bp_4:
        v3 = parse_ignoring (lambda : parse_string ("["))
        bp_4 = not v3
    if not bp_4:
        bp_6 = declare (False)
        v5 = declare (None)
        if not bp_6:
            bp_8 = declare (False)
            v7 = declare (None)
            if not bp_8:
                v7 = parse_ignoring (lambda :  KV ())
                bp_8 = not v7
            v5 = v7
            bp_6 = v7
            bp_6 = v5
        if not bp_6:
            bp_10 = declare (False)
            v9 = declare (None)
            if not bp_10:
                v9 = parse_ignoring (lambda :  Object ())
                bp_10 = not v9
            v5 = v9
            bp_6 = v9
            bp_6 = v5
        v3 = v5
        bp_4 = bp_6
        while v5:
            bp_6 = False
            if not bp_6:
                bp_12 = declare (False)
                v11 = declare (None)
                if not bp_12:
                    v11 = parse_ignoring (lambda :  KV ())
                    bp_12 = not v11
                v5 = v11
                bp_6 = v11
                bp_6 = v5
            if not bp_6:
                bp_14 = declare (False)
                v13 = declare (None)
                if not bp_14:
                    v13 = parse_ignoring (lambda :  Object ())
                    bp_14 = not v13
                v5 = v13
                bp_6 = v13
                bp_6 = v5
        bp_4 = not v3
    if not bp_4:
        v3 = parse_ignoring (lambda : parse_string ("]"))
        bp_4 = not v3
    v2 = v3
    bp_syn1 = v3
    if v2:
        return accept ("Array")
    else:
        return fail ("Array")
def Object ():
    begin ("Object")
    bp_syn1=declare(False)
    v2=declare(False)
    bp_4 = declare (False)
    v3 = declare (None)
    if not bp_4:
        v3 = parse_ignoring (lambda : parse_string ("{"))
        bp_4 = not v3
    if not bp_4:
        v3 = parse_ignoring (lambda :  KV ())
        bp_4 = not v3
    while v3:
        bp_4 = False
        v3 = parse_ignoring (lambda :  KV ())
    if not bp_4:
        v3 = parse_ignoring (lambda : parse_string ("}"))
        bp_4 = not v3
    v2 = v3
    bp_syn1 = v3
    if v2:
        return accept ("Object")
    else:
        return fail ("Object")
def KV ():
    begin ("KV")
    bp_syn1=declare(False)
    v2=declare(False)
    bp_4 = declare (False)
    v3 = declare (None)
    if not bp_4:
        v3 = parse_ignoring (lambda :  keystring ())
        bp_4 = not v3
    if not bp_4:
        v3 = parse_ignoring (lambda : parse_string (":"))
        bp_4 = not v3
    if not bp_4:
        bp_6 = declare (False)
        v5 = declare (None)
        if not bp_6:
            bp_8 = declare (False)
            v7 = declare (None)
            if not bp_8:
                v7 = parse_ignoring (lambda :  Array ())
                bp_8 = not v7
            v5 = v7
            bp_6 = v7
            bp_6 = v5
        if not bp_6:
            bp_10 = declare (False)
            v9 = declare (None)
            if not bp_10:
                v9 = parse_ignoring (lambda :  Object ())
                bp_10 = not v9
            v5 = v9
            bp_6 = v9
            bp_6 = v5
        if not bp_6:
            bp_12 = declare (False)
            v11 = declare (None)
            if not bp_12:
                v11 = parse_ignoring (lambda :  string ())
                bp_12 = not v11
            v5 = v11
            bp_6 = v11
            bp_6 = v5
        if not bp_6:
            bp_14 = declare (False)
            v13 = declare (None)
            if not bp_14:
                v13 = parse_ignoring (lambda :  emptyString ())
                bp_14 = not v13
            v5 = v13
            bp_6 = v13
            bp_6 = v5
        if not bp_6:
            bp_16 = declare (False)
            v15 = declare (None)
            if not bp_16:
                v15 = parse_ignoring (lambda :  number ())
                bp_16 = not v15
            v5 = v15
            bp_6 = v15
            bp_6 = v5
        v3 = v5
        bp_4 = bp_6
        bp_4 = not v3
    v2 = v3
    bp_syn1 = v3
    if v2:
        return accept ("KV")
    else:
        return fail ("KV")
def string ():
    begin ("string")
    bp_lex1=declare(False)
    v2=declare(False)
    bp_4 = declare (False)
    v3 = declare (None)
    if not bp_4:
        v3 = parse_string ("\"")
        bp_4 = not v3
    if not bp_4:
        v3 =  strchar ()
        bp_4 = not v3
    while v3:
        bp_4 = False
        v3 =  strchar ()
    if not bp_4:
        v3 = parse_string ("\"")
        bp_4 = not v3
    v2 = v3
    bp_lex1 = v3
    if v2:
        return accept ("string")
    else:
        return fail ("string")
def strchar ():
    begin ("strchar")
    bp_lex1=declare(False)
    v2=declare(False)
    bp_4 = declare (False)
    v3 = declare (None)
    if not bp_4:
        v3 = not parse_string ("\"")
        bp_4 = not v3
    if not bp_4:
        v3 =  any ()
        bp_4 = not v3
    v2 = v3
    bp_lex1 = v3
    if v2:
        return accept ("strchar")
    else:
        return fail ("strchar")
def keystring ():
    begin ("keystring")
    bp_lex1=declare(False)
    v2=declare(False)
    bp_4 = declare (False)
    v3 = declare (None)
    if not bp_4:
        v3 =  string ()
        bp_4 = not v3
    v2 = v3
    bp_lex1 = v3
    if v2:
        return accept ("keystring")
    else:
        return fail ("keystring")
def emptyString ():
    begin ("emptyString")
    bp_lex1=declare(False)
    v2=declare(False)
    bp_4 = declare (False)
    v3 = declare (None)
    if not bp_4:
        v3 = parse_string ("\"")
        bp_4 = not v3
    if not bp_4:
        v3 = parse_string ("\"")
        bp_4 = not v3
    v2 = v3
    bp_lex1 = v3
    if v2:
        return accept ("emptyString")
    else:
        return fail ("emptyString")
def number ():
    begin ("number")
    bp_lex1=declare(False)
    v2=declare(False)
    bp_4 = declare (False)
    v3 = declare (None)
    if not bp_4:
        bp_6 = declare (False)
        v5 = declare (None)
        if not bp_6:
            bp_8 = declare (False)
            v7 = declare (None)
            if not bp_8:
                v7 = parse_string ("0")
                bp_8 = not v7
            v5 = v7
            bp_6 = v7
            bp_6 = v5
        if not bp_6:
            bp_10 = declare (False)
            v9 = declare (None)
            if not bp_10:
                v9 = parse_string ("1")
                bp_10 = not v9
            v5 = v9
            bp_6 = v9
            bp_6 = v5
        if not bp_6:
            bp_12 = declare (False)
            v11 = declare (None)
            if not bp_12:
                v11 = parse_string ("2")
                bp_12 = not v11
            v5 = v11
            bp_6 = v11
            bp_6 = v5
        if not bp_6:
            bp_14 = declare (False)
            v13 = declare (None)
            if not bp_14:
                v13 = parse_string ("3")
                bp_14 = not v13
            v5 = v13
            bp_6 = v13
            bp_6 = v5
        if not bp_6:
            bp_16 = declare (False)
            v15 = declare (None)
            if not bp_16:
                v15 = parse_string ("4")
                bp_16 = not v15
            v5 = v15
            bp_6 = v15
            bp_6 = v5
        if not bp_6:
            bp_18 = declare (False)
            v17 = declare (None)
            if not bp_18:
                v17 = parse_string ("5")
                bp_18 = not v17
            v5 = v17
            bp_6 = v17
            bp_6 = v5
        if not bp_6:
            bp_20 = declare (False)
            v19 = declare (None)
            if not bp_20:
                v19 = parse_string ("6")
                bp_20 = not v19
            v5 = v19
            bp_6 = v19
            bp_6 = v5
        if not bp_6:
            bp_22 = declare (False)
            v21 = declare (None)
            if not bp_22:
                v21 = parse_string ("7")
                bp_22 = not v21
            v5 = v21
            bp_6 = v21
            bp_6 = v5
        if not bp_6:
            bp_24 = declare (False)
            v23 = declare (None)
            if not bp_24:
                v23 = parse_string ("8")
                bp_24 = not v23
            v5 = v23
            bp_6 = v23
            bp_6 = v5
        if not bp_6:
            bp_26 = declare (False)
            v25 = declare (None)
            if not bp_26:
                v25 = parse_string ("9")
                bp_26 = not v25
            v5 = v25
            bp_6 = v25
            bp_6 = v5
        v3 = v5
        bp_4 = bp_6
        while v5:
            bp_6 = False
            if not bp_6:
                bp_28 = declare (False)
                v27 = declare (None)
                if not bp_28:
                    v27 = parse_string ("0")
                    bp_28 = not v27
                v5 = v27
                bp_6 = v27
                bp_6 = v5
            if not bp_6:
                bp_30 = declare (False)
                v29 = declare (None)
                if not bp_30:
                    v29 = parse_string ("1")
                    bp_30 = not v29
                v5 = v29
                bp_6 = v29
                bp_6 = v5
            if not bp_6:
                bp_32 = declare (False)
                v31 = declare (None)
                if not bp_32:
                    v31 = parse_string ("2")
                    bp_32 = not v31
                v5 = v31
                bp_6 = v31
                bp_6 = v5
            if not bp_6:
                bp_34 = declare (False)
                v33 = declare (None)
                if not bp_34:
                    v33 = parse_string ("3")
                    bp_34 = not v33
                v5 = v33
                bp_6 = v33
                bp_6 = v5
            if not bp_6:
                bp_36 = declare (False)
                v35 = declare (None)
                if not bp_36:
                    v35 = parse_string ("4")
                    bp_36 = not v35
                v5 = v35
                bp_6 = v35
                bp_6 = v5
            if not bp_6:
                bp_38 = declare (False)
                v37 = declare (None)
                if not bp_38:
                    v37 = parse_string ("5")
                    bp_38 = not v37
                v5 = v37
                bp_6 = v37
                bp_6 = v5
            if not bp_6:
                bp_40 = declare (False)
                v39 = declare (None)
                if not bp_40:
                    v39 = parse_string ("6")
                    bp_40 = not v39
                v5 = v39
                bp_6 = v39
                bp_6 = v5
            if not bp_6:
                bp_42 = declare (False)
                v41 = declare (None)
                if not bp_42:
                    v41 = parse_string ("7")
                    bp_42 = not v41
                v5 = v41
                bp_6 = v41
                bp_6 = v5
            if not bp_6:
                bp_44 = declare (False)
                v43 = declare (None)
                if not bp_44:
                    v43 = parse_string ("8")
                    bp_44 = not v43
                v5 = v43
                bp_6 = v43
                bp_6 = v5
            if not bp_6:
                bp_46 = declare (False)
                v45 = declare (None)
                if not bp_46:
                    v45 = parse_string ("9")
                    bp_46 = not v45
                v5 = v45
                bp_6 = v45
                bp_6 = v5
        bp_4 = not v3
    v2 = v3
    bp_lex1 = v3
    if v2:
        return accept ("number")
    else:
        return fail ("number")
