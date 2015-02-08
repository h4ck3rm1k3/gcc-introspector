"""
test creating peewee models and then loading them with data!
"""
import pprint
from Readme import TreeDefSourceFile
from Readme import NodeBase, DefNodeClass, DefTreeCode
from peewee_adaptor import PeeWeeAdaptor

def test_klass(c, **args):
    pa = PeeWeeAdaptor()
    pc = pa.create_adaptor_class(c)
    # create an object of this
    pprint.pprint(args)
    o = c(**args)
   
    # put into the db
    pc.append(o)
    
def python_base_classes_test():
    """
    test the base classes
    """

    test_klass( DefNodeClass, node_class="funky")

    test_klass( DefTreeCode,
                macro_name="ABC",
                struct_name="SomeStruct", 
                node_class='funky',
                argc=10)
    for c in (            
            NodeBase,
    ):
        test_klass(c)

        
def python_classes_test():
    x = TreeDefSourceFile()
    for t in x.tree_codes():
        c = t.create_python_class()
        test_klass(c)

def python_node_classes_test():
    x = TreeDefSourceFile()
    for t in x.node_classes():
        c = t.create_python_class()
        test_klass(c)


if __name__ == '__main__':
    python_base_classes_test()
    python_node_classes_test()
    python_classes_test()

