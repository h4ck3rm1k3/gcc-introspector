"""
Module for generating a python class
"""
import sys
import types

class PythonClassGen(object):
    """
    base class for creating python classes(types) and modules on the fly
    
    you need to override :

    class_name : the name of the class
    base_classes : the list of base classes
    object_data : a dict of key values to create the object
    module_name : the name of the module
    class_doc : the doc string for the class
    """
    def transform_class_name(self, name):
        return ''.join([n.title() for n in name.split("_")])

    def create_python_class(self):
        class_name = self.class_name()
        base_classes = self.base_classes()
        object_data = self.object_data()
        klass = type(class_name, base_classes,object_data)
        #klass.__name__ = self.class_name()
        klass.__module__ = self.module_name()
        klass.__doc__ = self.class_doc()

        if klass.__module__ not in sys.modules:
            # create the module if needed
            module = types.ModuleType(klass.__module__, "dynamically created module")
            sys.modules[klass.__module__] = module

        # now register the class in the module
        module = sys.modules[klass.__module__]
        setattr(module, klass.__name__, klass)

        return klass
