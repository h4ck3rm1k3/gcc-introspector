# class NodeType(object):
#     """
#     node type enum that is used in the tree node class
#     """
    

# class Field(object):
#     """
#     declares a field in a class
#     """
#     def __init__(self,ntype):
#         pass

# class TreeNode(object):
#     "base class of all trees"
#     node_type = Field(NodeType)

# class ErrorMark(TreeNode):
#     "error handling"

# class Identifier(TreeNode):
#     'id'


# class IdentifierNode(Identifier):
#     'an id in the program'

# class OpIdentifier(Identifier):
#     ''

# class TreeList(TreeNode):
#     ' a list of nodes, also used as a general-purpose "container object" '

# class TreeVec(TreeNode):
#     ''

# class Block(TreeNode):
#     ''

# class TreeType(TreeNode):
#     ' information about types '

# class VoidType(TreeType):
#     ''

# class IntegerType(TreeType):
#     ''

# class RecordType(TreeType):
#     ''

# class FunctionType(TreeType):
#     ''

#      # |    \--- LANG_TYPE  { for language-specific extensions }
# class TreeConst(TreeNode):
#     ''

# class IntegerConst(TreeConst):
#     'an integer constant'

# class RealConst(TreeConst):
#     ''

# class StringConst(TreeConst):
#     ''

# class ComplexConst(TreeConst):
#     ''

# class Declaration(TreeNode):
#     ''

# class FunctionDecl(Declaration):
#     ''

# class TypeDecl(Declaration):
#     ''
#      # |    \--- VAR_DECL


# class Reference(TreeNode):
#     ''


# class ComponentRef(Reference):
#     ''
#      # |    \--- ARRAY_REF
#      # |

# class Constructor(TreeNode):
#     ''
#      # \--- (expression)
#      #      |
#      #      |--- MODIFY_EXPR  { assignment }
#      #      |
#      #      |--- PLUS_EXPR  { addition }
#      #     ...
#      #      |
#      #      |--- CALL_EXPR  { procedure/function call }
#      #      |
#      #      |--- GOTO_EXPR
#      #      |
#      #      \--- LOOP_EXPR  { for all loops }
