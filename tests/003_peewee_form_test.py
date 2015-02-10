"""
test creating peewee models and then loading them with data!
"""
import pprint
import sys
sys.path.append('/home/mdupont/experiments/jinja2/')
sys.path.append('../flask/')
sys.path.append('../werkzeug/')
sys.path.append('../itsdangerous/')
sys.path.append('../wtf-peewee/')
sys.path.append('../wtforms/')
import pdb;

from Readme import TreeDefSourceFile
from Readme import NodeBase, DefNodeClass, DefTreeCode
from peewee_adaptor import PeeWeeAdaptor
from peewee_wtf_adaptor import WTFPeeWeeAdaptor
import flask

from flask.globals import session, _request_ctx_stack, _app_ctx_stack, \
     current_app, request

def main():
    app = flask.Flask(__name__)
    # the classes to run
    classes = [DefNodeClass]
    pa = PeeWeeAdaptor()
    pa.database()
    pa.db.connect()

    class AppCtx:
        def __init__(self,app):
            self.app=app
            self.g= "g"
    class FakeReq:
        class Adaptor:
            def build(self, endpoint, values, method, force_external):
                return None
        class Session:
            pass

        class Form:
            def getall(self):
                return {}

            def __len__(self):
                return 0

        class Req:
            def __init__(self):
                self.blueprint = "Funky"
                self._is_old_module=False
                self.method = "POST"
                self.form= FakeReq.Form()
        def __init__(self):
            self.url_adapter = FakeReq.Adaptor()
            self.request =  FakeReq.Req()
            self.session =  FakeReq.Session()

    forms = []
    for c in classes:
        pc = pa.create_adaptor_class(c)
        pa.db.create_tables([pc._model_class], safe=True)
        name = c.__name__
        wtf = WTFPeeWeeAdaptor(name,pc)

        # install the item in the app
        wtf.install_adaptor_class(app) 
        forms.append(wtf)
        _app_ctx_stack.push(AppCtx(app))
        request = FakeReq() 
        _request_ctx_stack.push(request)

        pdb.set_trace();

        url = flask.url_for('edit', id=123)
        print("URL:" + str(url))
        #wtf.add()
        #wtf.edit(1)

    for rule in app.url_map.iter_rules():
        print("rule  : " + str(rule))
        print("Endpoint  : " + rule.endpoint)
        print("Route  : " + rule.rule)
        print("Methods: " + str(rule.methods) )

    app.config['EXPLAIN_TEMPLATE_LOADING']=True
    

if __name__ == '__main__':
    main()

