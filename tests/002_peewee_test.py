"""
test creating peewee models and then loading them with data!
"""
import pprint
from Readme import TreeDefSourceFile
from Readme import NodeBase, DefNodeClass, DefTreeCode
from peewee_adaptor import PeeWeeAdaptor

pa = PeeWeeAdaptor()

def test_klass(c, **args):

    pc = pa.create_adaptor_class(c)

    pa.db.create_tables([pc._model_class], safe=True)

    # create an object of this
    #pprint.pprint(args)
    o = c(**args)
    
    # put into the db
    pc.append(o)
    
def python_base_classes_test():
    """
    test the base classes
    """

    test_klass( DefNodeClass, node_class="funky")
    return

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
    pa.database()
    pa.db.connect()
    
    python_base_classes_test()
    if False:
        python_node_classes_test()
        python_classes_test()

