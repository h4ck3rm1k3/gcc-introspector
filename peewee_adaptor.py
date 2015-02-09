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
from peewee import SqliteDatabase


class PeeWeeFieldAdaptor :

    def __init__(self, source_property,
                 name=None,
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

        def doeval(x):
            if x == 'False':
                return False
            if x == 'True':
                return True
            elif x == 'None':
                return None
            else:
                return x

        self._name = name
        self._source_property = source_property
        self._field_class = peewee.__dict__[db_type]

        self._field_obj = self._field_class(
            null=doeval(db_null),
            index=doeval(db_index),
            unique=doeval(db_unique),
            verbose_name=doeval(db_verbose_name),
            help_text=doeval(db_help_text),
            db_column=doeval(db_column),
            default=doeval(db_default),
            choices=doeval(db_choices),
            primary_key=doeval(db_primary_key),
            sequence=doeval(db_sequence),
            constraints=doeval(db_constraints),
            schema=doeval(db_schema),
            max_length=doeval(db_max_length)
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
    def create_python_class(self):
        x = super(PeeWeeModuleClassGen,self).create_python_class()
        for f in self._fields :
            meta = getattr(x, '_meta')
            #pprint.pprint(meta.fields)
            #meta.fields[f._name]=f._field_obj
            f._field_obj.add_to_class(x, name=f._name)

        return x

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

    def database(self):
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
