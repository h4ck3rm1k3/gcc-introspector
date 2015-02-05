"""
GCC node type micro service

see tree.def
source http://www.gnu-pascal.de/gpc/Tree-nodes.html
"""

class TreeNode(object):
    "base class of all trees"

class ErrorMark(TreeNode):
    "error handling"


class Identifier(TreeNode):
    'id'


class IdentifierNode(Identifier):
    'an id in the program'

class OpIdentifier(Identifier):
    ''

class TreeList(TreeNode):
    ' a list of nodes, also used as a general-purpose "container object" '

class TreeVec(TreeNode):
    ''

class Block(TreeNode):
    ''

class TreeType(TreeNode):
    ' information about types '

class VoidType(TreeType):
    ''

class IntegerType(TreeType):
    ''

class RecordType(TreeType):
    ''

class FunctionType(TreeType):
    ''

     # |    \--- LANG_TYPE  { for language-specific extensions }
class TreeConst(TreeNode):
    ''

class IntegerConst(TreeConst):
    'an integer constant'

class RealConst(TreeConst):
    ''

class StringConst(TreeConst):
    ''

class ComplexConst(TreeConst):
    ''

class Declaration(TreeNode):
    ''

class FunctionDecl(Declaration):
    ''

class TypeDecl(Declaration):
    ''
     # |    \--- VAR_DECL


class Reference(TreeNode):
    ''


class ComponentRef(Reference):
    ''
     # |    \--- ARRAY_REF
     # |

class Constructor(TreeNode):
    ''
     # \--- (expression)
     #      |
     #      |--- MODIFY_EXPR  { assignment }
     #      |
     #      |--- PLUS_EXPR  { addition }
     #     ...
     #      |
     #      |--- CALL_EXPR  { procedure/function call }
     #      |
     #      |--- GOTO_EXPR
     #      |
     #      \--- LOOP_EXPR  { for all loops }
