"""
peewee adaptor

takes a dynamically generated class  and turns it into a peewee database model
"""
import sys
sys.path.append('../peewee/')
sys.path.append('../flask/')
import peewee
import pprint
from docutils.core import publish_doctree
import docutils.nodes
from python_class_gen import PythonClassGen
from flask import Flask
from wtfpeewee.orm import model_form

class WTFPeeWeeAdaptor :
    """
    create routes
    """
    def __init__(self, name, db_class):
        """
        """
        self._name = name
        self._db_class = db_class
        self._form_class = model_form(self._db_class._model_class)

    def edit(self, record_id):
        try:
            obj = self._db_class._model_class.get(id=record_id)
        except Exception as exp:
            print(exp)
            raise exp

        if request.method == 'POST':
            form = self.form_class(request.form, obj=entry)
            if form.validate():
                form.populate_obj(entry)
                obj.save()
                flash('Your entry has been saved')
        else:
            form = self.form_class(obj=obj)
        return render_template(self._name + '/edit.html',
                               form=form,
                               entry=entry)


    def install_adaptor_class(self, app):
        """
        creates a website
        """
        rule = '/{name}/<int:record_id>/'.format(
                name=self._name
            )
        print("Rule:"+rule)
        app.add_url_rule(
            rule = rule,
            view_func=self.edit,
            methods=['GET', 'POST']
        )
