## builtins
def debugprogress ():
    return False
def debugtrace ():
    return True

class StringBuffer ():
    def __init__ (self):
        self.buff = ""
        self.bx = 0
        self.marks = []
    def set_input (self, s):
        self.buff = s
    def push_mark (self):
        self.marks.append (self.bx)
    def pop_mark (self):
        self.marks.pop ()
    def rewind (self):
        self.bx = self.marks.pop ()
    def accept_char (self):
        self.bx += 1
    def overrun (self):
        return self.bx >= len (self.buff)
    def is_space (self):
        if self.overrun ():
            return False
        elif self.buff [self.bx] == " " or self.buff [self.bx] == "," or self.buff [self.bx] == "\n" :
            return True
    def look (self):
        if self.overrun ():
            bifail (e)
        else:
            return self.buff [self.bx]
    def parse_char (self, c):
        if self.overrun ():
            return False
        if c == self.buff [self.bx]:
            self.accept_char ()
            return True
        return False

class Indentation ():
    def __init__ (self):
        self.indent = 0
        self.prefix = ''
    def ind (self):
        self.indent += 1
    def out (self):
        self.indent -= 1
    def pr (self):
        if debugprogress ():
            print (" " * self.indent, end="")
            print (self.prefix, end="")
        pass

    
buffer = StringBuffer ()
indent = Indentation ()

def parse_debug_prefix (s):
    global indent
    indent.prefix = s
    
def fail (s):
    global buffer
    global indent
    indent.out ()
    indent.pr ()
    if debugtrace ():
        print (f'fail {s}')
    buffer.rewind ()

def begin (s):
    global buffer
    global indent
    indent.pr ()
    indent.ind ()
    if debugprogress ():
        print (f'begin {s} {buffer.buff[buffer.bx:10].replace('\n', '⤶').replace(' ', '␣')}')
    elif debugtrace ():
        print (f'begin {s}')
    buffer.push_mark ()

def accept (s):
    global buffer
    global indent
    indent.out ()
    indent.pr ()
    prev = buffer.pop_mark ()
    if debugprogress () or debugtrace ():
        print (f'accept {s}')

def parse (f):
    if f ():
        return True
    return False

def parse_string (s):
    global buffer
    if debugprogress ():
        print (f'parse_string {s} in {buffer.buff[buffer.bx:10].replace('\n', '⤶').replace(' ', '␣')}')
    elif debugtrace ():
        print (f'parse_string {s}')
    i = 0
    while i < len (s):
        if debugprogress ():
            print (f' continue parse_string i={i} len(s)={len(s)} {s [i]} in {buffer.buff[buffer.bx:10].replace('\n', '⤶').replace(' ', '␣')}')
        if buffer.parse_char (s [i]):
            i += 1
            continue
        else:
            if debugtrace ():
                print (f' fail parse_string {s} want {s} in {buffer.buff[buffer.bx:10].replace('\n', '⤶').replace(' ', '␣')}')
            return False
    if debugtrace ():
        print (f' exit parse_string {s}')
    return True
    
def parse_upto (c):
    global buffer
    if debugtrace ():
        print (f'parse_upto {c}')
    while True:
        if buffer.overrun ():
            return False
        else:
            if c == buffer.look ():
                break
            else:
                buffer.accept_char ()
    return True

def parse_range (first, last):
    global buffer
    if debugtrace ():
        print (f'parse_range')
    if buffer.look () >= first and buffer.look () <= last:
        buffer.accept_char ()
        return True
    else:
        return False

def parse_ignore ():
    global buffer
    if debugprogress ():
        print (f'parse_ignore {buffer.buff[buffer.bx:10].replace('\n', '⤶').replace(' ', '␣')}')
    elif debugtrace ():
        print (f'parse_ignore')
    while (buffer.is_space ()):
        buffer.accept_char ()
    if debugprogress ():
        print (f' exit parse_ignore {buffer.buff[buffer.bx:10].replace('\n', '⤶').replace(' ', '␣')}')

def parse_one_or_more (f):
    if debugtrace ():
        print (f'parse_one_or_more {f}')
    parse_debug_prefix ('+')
    if f ():
        while True:
            print (f'  >>loop on {f}')
            if f ():
                continue
            else:
                parse_debug_prefix ('')
                return True
    else:
        parse_debug_prefix ('')
        return False
    
def parse_either (flist):
    if debugtrace ():
        print (f'parse_either {flist}')
    parse_debug_prefix ('|')
    while True:
        if debugtrace ():
            print (f'  continue parse_either len=({len(flist)}) {flist}')
        f = flist [0]
        if f ():
            parse_debug_prefix ('')
            return True
        elif flist:
            if len (flist) > 1:
                flist = flist [1:]
            else:
                parse_debug_prefix ('')
                return False
        else:
            parse_debug_prefix ('')
            return False
    raise Exception ("internal error: should not have reached this point")

def parse_set_input (s):
    buffer.set_input (s)
