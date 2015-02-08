
"""
peewee adaptor

takes a dynamically generated class  and turns it into a peewee database model 
"""
import sys
sys.path.append('../peewee/')
import peewee
import pprint 

class PeeWeeClassAdaptor :
    def __init__(self, source_class):
        self._source_class = source_class

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

    def create_adaptor_class(self, classobj):
        """
        describe the class and create a new peewee compatible adaptor class 
        for bidirectional communication with the original
        """
        d = classobj.__dict__
        for x in d:
            v = d[x]
            print ("debug",x, v)
            if isinstance(v,property): # property
                print("Prop name",x,v.__doc__)
                #print(help(v))
                #pprint.pprint (["prop",x,v,y,vv])                
                   
        #print (d)
            #print(help(classobj))

        pw = PeeWeeClassAdaptor(classobj)

        return pw
