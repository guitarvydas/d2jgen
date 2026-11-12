blocks:
1: parse_string "(" ; result-> 2.v
2: Seq Fork ; fail-> 12.v, retv-> 3.v
3: parse string "|" ; result-> 4.v
4: Seq Fork ; fail-> 6.v, retv-> 5.v
5: parse call x() ; result-> 6.v
6: Alt Fork ; ok->10.v, retv->7.v
7: parse string "|" ; result->8.v
8: Seq Fork ; fail->12.v, retv->9.v
9: parse call y() ; result->10.v
10: Seq Fork ; fail->12.v, retv->11.v
11: parse call z(); result->12.v
12: Final ; fail->fail, ok->ok