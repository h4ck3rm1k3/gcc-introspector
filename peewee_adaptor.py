
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
class PeeWeeClassAdaptor :
    def __init__(self, source_class, fields):
        self._source_class = source_class
        self._fields = fields
        
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
        pprint.pprint(w.fields)
        #TODO:
        
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
