import sys
sys.path.append('../flask/')
sys.path.append('../werkzeug/')
sys.path.append('../itsdangerous/')
sys.path.append('../wtf-peewee/')
sys.path.append('../wtforms/')


from peewee_wtf_adaptor import WTFPeeWeeAdaptor
from peewee_adaptor import PeeWeeAdaptor
from Readme import NodeBase, DefNodeClass, DefTreeCode
from flask import Flask

def main():
    app = Flask(__name__)
    # the classes to run
    classes = [DefNodeClass]
    pa = PeeWeeAdaptor()
    pa.database()
    pa.db.connect()

    forms = []
    for c in classes:
        pc = pa.create_adaptor_class(c)
        pa.db.create_tables([pc._model_class], safe=True)
        name = c.__name__
        wtf = WTFPeeWeeAdaptor(name,pc)

        # install the item in the app
        wtf.install_adaptor_class(app) 

        forms.append(wtf)

    for rule in app.url_map.iter_rules():
        print("rule  : " + str(rule))
        print("Endpoint  : " + rule.endpoint)
        print("Route  : " + rule.rule)
        print("Methods: " + str(rule.methods) )

    app.debug = True
    app.run()

if __name__ == "__main__":
    main()
