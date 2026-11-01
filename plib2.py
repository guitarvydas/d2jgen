## builtins
def debugprogress ():
    return False
def debugtrace ():
    return False

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
        elif self.buff [self.bx] == " " or self.buff [self.bx] == "," or self.buff [self.bx] == "\n" or self.buff [self.bx] == "\t" :
            return True
    def look (self):
        if self.overrun ():
            bifail (e)
        else:
            return self.buff [self.bx]
    def buffrepr (self):
        return f"<{self.bx}>{self.buff[self.bx:10].replace('\n', '⤶').replace(' ', '␣').replace('\t', '⇢')}"
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
        if debugprogress () or debugtrace ():
            print (" " * self.indent, end="")
            print (self.prefix, end="")
        pass

    
buffer = StringBuffer ()
indent = Indentation ()

def parse_debug_prefix (s):
    global indent
    indent.prefix = s

def pbuffrepr (s):
    global buffer
    print (f'{s}{buffer.buffrepr()}')
    
def fail (s):
    global buffer
    global indent
    indent.out ()
    indent.pr ()
    if debugtrace ():
        print (f'fail {s}')
    buffer.rewind ()
    return False

def begin (s):
    global buffer
    global indent
    indent.pr ()
    indent.ind ()
    if debugprogress ():
        print (f'begin {s} {buffer.buffrepr()}')
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
    return True

def parse (f):
    if f ():
        return True
    return False

def parse_string (s):
    global buffer
    i = 0
    while i < len (s):
        if buffer.parse_char (s [i]):
            i += 1
            continue
        else:
            return False
    return True
    
def parse_upto (c):
    global buffer
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
    if buffer.look () >= first and buffer.look () <= last:
        buffer.accept_char ()
        return True
    else:
        return False

def parse_ignore ():
    global buffer
    while (buffer.is_space ()):
        buffer.accept_char ()

def parse_one_or_more (f):
    parse_debug_prefix ('+')
    if f ():
        while True:
            if f ():
                continue
            else:
                parse_debug_prefix ('')
                return True
    else:
        parse_debug_prefix ('')
        return False
    
def parse_either (flist):
    parse_debug_prefix ('|')
    while True:
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
