from plib2 import StringBuffer, fail, accept, begin, parse_ignore, parse_string, parse_one_or_more, parse_either, parse_upto, parse_range, parse_set_input, pbuffrepr

import generated_parser

with open("test.txt", "r", encoding="utf-8") as f:
    stest = f.read()
    parse_set_input (stest)
    begin ("test")
    if main ():
        accept ("test")
        print (f'success')
    else:
        fail ("test")
        print (f'fail')
