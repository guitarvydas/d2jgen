from plib2 import *
from mock import *

with open("test.txt", "r", encoding="utf-8") as f:
    stest = f.read()
    parse_set_input (stest)
    begin ("testmock")
    ok = Rule ()
    if ok:
        accept ("testmock")
        print (f'success', end='')
    else:
        fail ("testmock")
        print (f'fail', end='')
    pbuffrepr (": ")
