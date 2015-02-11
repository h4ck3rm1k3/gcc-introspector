import sys
sys.path.append('../flask/')
sys.path.append('../werkzeug/')
sys.path.append('../itsdangerous/')
sys.path.append('../wtf-peewee/')
sys.path.append('../wtforms/')


from peewee_wtf_adaptor import WTFPeeWeeAdaptor
from peewee_adaptor import PeeWeeAdaptor
from Readme import NodeBase, DefNodeClass, DefTreeCode, TreeDefSourceFileApi
from flask import Flask
import logging

def main():
    logging.warn("Main")
    app = Flask(__name__)
    app.debug = True

    # the classes to run
    classes = [
        DefNodeClass,  # what is a node class
        TreeDefSourceFileApi # how to get them into the system
    ]
    pa = PeeWeeAdaptor()
    pa.database()
    pa.db.connect()

    forms = []
    for target_class in classes:
        name = target_class.__name__
        peewee_adaptor_class = pa.create_adaptor_class(target_class)

        pa.db.create_tables([peewee_adaptor_class._model_class], safe=True)

        wtf_adaptor = WTFPeeWeeAdaptor(name,peewee_adaptor_class)

        # install the item in the app
        wtf_adaptor.install_adaptor_class(app)
        forms.append(wtf_adaptor)

        # install the adaptors into the original class so we can use them later
        target_class._peewee_adaptor_class = peewee_adaptor_class
        target_class._wtf_adaptor = wtf_adaptor


    for rule in app.url_map.iter_rules():
         #print(dir(rule))
         #print(rule.__dict__)
         print("Rule  : " + str(rule))
         print("    Endpoint  : " + rule.endpoint)
         print("    Host  : " + str(rule.host))
         print("    Route  : " + rule.rule)
         print("    Methods: " + str(rule.methods) )

    app.config['EXPLAIN_TEMPLATE_LOADING']=True


    app.run()

if __name__ == "__main__":
    main()
