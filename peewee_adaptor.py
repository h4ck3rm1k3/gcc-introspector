
"""
peewee adaptor

takes a dynamically generated class  and turns it into a peewee database model 
"""
import sys
sys.path.append('../peewee/')
import peewee
import pprint 
from docutils.core import publish_doctree
import docutils.nodes
#import xml.etree.ElementTree as etree
from python_class_gen import PythonClassGen

class PeeWeeFieldAdaptor :
    def __init__(self, source_property,
                 name=False, 
                 db_type="TextField",
                 db_null=False, 
                 db_index=False, 
                 db_unique=False,
                 db_verbose_name=None, 
                 db_help_text=None, 
                 db_column=None,
                 db_default=None, 
                 db_choices=None, 
                 db_primary_key=False, 
                 db_sequence=None,
                 db_constraints=None, 
                 db_schema=None,
                 db_max_length=None,
                 ):
        self._source_property = source_property
        self._field_class = peewee.__dict__[db_type]
        self._field_obj = self._field_class(
            null=db_null, 
            index=db_index, 
            unique=db_unique,
            verbose_name=db_verbose_name, 
            help_text=db_help_text, 
            db_column=db_column,
            default=db_default, 
            choices=db_choices, 
            primary_key=db_primary_key, 
            sequence=db_sequence,
            constraints=db_constraints, 
            schema=db_schema,
            max_length=db_max_length,
        )

class PeeWeeModuleClassGen(PythonClassGen):
    def __init__(self, 
                 src_class_name,
                 fields):
        self._src_class_name = src_class_name
        self._fields = fields

    def class_name(self):
        return "DB" + self._src_class_name

    def base_classes(self):
        return (peewee.Model,)

    def object_data(self):
        return {}

    def module_name(self):
        return "peeweedb"

    def class_doc(self):
        return "TODO"

class PeeWeeClassAdaptor :
    def __init__(self, source_class, fields):
        self._source_class = source_class
        print()
        self._fields = fields
        class_gen = PeeWeeModuleClassGen(
            src_class_name=source_class.__name__,
            fields = fields,
        )
        self._model_class = class_gen.create_python_class()
        #Model
        # now create the peewee 
        
    def append(self,obj):
        pass

class PeeWeeAdaptor :
    """
    create a dedicate peewee class that describes this class in a peewee like standard manner
    we will use this for generated classes as well, so needs to be flexable
    """
    def __init__(self):
        self.db = None

    def database():
        self.db = SqliteDatabase('example.db')

    def create_adaptor_field(self, classobj, prop):
        doc = prop.__doc__
        doctree = publish_doctree(doc)
        class Walker:
            def __init__(self, doc):
                self.document = doc
                self.fields = {}
            def dispatch_visit(self,x):
                if isinstance(x, docutils.nodes.field):
                    field_name = x.children[0].rawsource
                    field_value = x.children[1].rawsource
                    self.fields[field_name]=field_value
        w = Walker(doctree)
        doctree.walk(w)
        #pprint.pprint(w.fields)
        return PeeWeeFieldAdaptor(prop, **w.fields)

        
    def create_adaptor_class(self, classobj):
        """
        describe the class and create a new peewee compatible adaptor class 
        for bidirectional communication with the original
        """
        d = classobj.__dict__
        fields = []
        for x in d:
            v = d[x]
            #print ("debug",x, v)
            if isinstance(v,property): # property
                #print("Prop name",x,v.__doc__)
                field = self.create_adaptor_field(classobj, v)
                fields.append(field)

        pw = PeeWeeClassAdaptor(classobj,fields)

        return pw
