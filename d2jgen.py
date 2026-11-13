from plib2 import *
def main ():
    begin ("main")
    r = True
    if r:
        r = a ()
    if r:
        r = b ()
    if r:
        r = c ()
    if r:
        return accept ("main")
    else:
        return fail ("main")
