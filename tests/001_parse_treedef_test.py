import pprint
from Readme import TreeDefSourceFile

def test_klass(c):
    print ("\n\n\n")
    for x in c.__dict__:
        pprint.pprint(c)
        pprint.pprint(c.__dict__)
        print(help(c))
        print (x, c.__dict__[x])

    # create an object of this
    o = c()

    pprint.pprint(o)
        
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
    python_node_classes_test()
    python_classes_test()
