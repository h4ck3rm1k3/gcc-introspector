import sys
sys.path.append('/mnt/data/home/mdupont/experiments/introspector/cpip/src')

from cpip.core import PpLexer, IncludeHandler
import re

def tree_codes(file_name):
    report = []
    #print('Processing:', )
    myH = IncludeHandler.CppIncludeStdOs(
        theUsrDirs=['proj/usr',],
        theSysDirs=['proj/sys',],
        )
    myLex = PpLexer.PpLexer(file_name, myH)
    stack = []
    for tok in myLex.ppTokens():
        if tok.t == '\n':
            code = ("".join(stack))
            if re.match(r'^\s+$',code):
                pass
            else:
                if code:
                    # macro name
                    # class name
                    # class of node
                    # arguments?
                    #print "CODE(%s)"% code;
                    m = re.match(r'DEFTREECODE\((\w+),\"(\w+)",(\w+),(\d)\)',code)
                    report.append(m.groups())
            stack = []
        else:
            if tok.t ==' ':
                pass
            elif re.match(r'^[\s\n\t]*$',tok.t):
                pass
            else:
                #print "TOK(%s)" % tok.t
                stack.append(tok.t)
    return report
