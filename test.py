from plib2 import *
from generated_parser import *

with open("test.txt", "r", encoding="utf-8") as f:
    stest = f.read()
    parse_set_input (stest)
    begin ("test")
    if Main ():
        accept ("test")
        print (f'success')
    else:
        fail ("test")
        print (f'fail')
