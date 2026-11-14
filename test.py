from plib2 import *
from d2jgen import *

with open("test.txt", "r", encoding="utf-8") as f:
    stest = f.read()
    parse_set_input (stest)
    begin ("test")
    ok = Main ()
    if ok:
        accept ("test")
        print (f'success', end='')
    else:
        fail ("test")
        print (f'fail', end='')
    pbuffrepr (": ")
