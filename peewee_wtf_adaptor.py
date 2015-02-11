"""
peewee adaptor

takes a dynamically generated class  and turns it into a peewee database model
"""
import sys
sys.path.append('/home/mdupont/experiments/jinja2/')
sys.path.append('../werkzeug/')
sys.path.append('../peewee/')
sys.path.append('../flask/')
import peewee
import pprint
from docutils.core import publish_doctree
import docutils.nodes
from python_class_gen import PythonClassGen
from flask import Flask
from wtfpeewee.orm import model_form
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import Blueprint
import logging
from flask.globals import session, _request_ctx_stack, _app_ctx_stack, \
     current_app, request

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

    def index(self):
        obj = self._db_class._model_class()
        objects = obj.select()
        return render_template(self._name + '/index.html', objects=objects)

    def add(self, **kwargs):
        #print(str(kwargs))
        obj = self._db_class._model_class()

        if request.method == 'POST':
            form = self._form_class(request.form, obj=obj)
            if form.validate():
                form.populate_obj(obj)
                obj.save()
                #flash('Successfully added %s' % obj, 'success')
                return redirect(url_for('.edit', record_id=obj.id))
                
        else:
            form = self._form_class(obj=obj)

        return render_template(self._name + '/add.html',
                               obj=obj, form=form)

    def edit(self, record_id):
        try:
            obj = self._db_class._model_class.get(id=record_id)
        except Exception as exp:
            print(exp)
            raise exp

        if request.method == 'POST':
            form = self._form_class(request.form, obj=obj)
            if form.validate():
                form.populate_obj(obj)
                obj.save()
                #flash('Your obj has been saved')
        else:
            form = self._form_class(obj=obj)
        return render_template(self._name + '/edit.html',
                               form=form,
                               obj=obj)

    def detail(self, record_id):
        try:
            obj = self._db_class._model_class.get(id=record_id)
        except Exception as exp:
            print(exp)
            raise exp

        form = self._form_class(obj=obj)

        return render_template(self._name + '/detail.html',
                               form=form,
                               obj=obj)


    def install_adaptor_class(self, app):
        """
        creates a website
        """

        # delegate to the db class to allow for installing of rules into flask
        #self._db_class.install_adaptor_class(app)
        logging.warn('Installing {name}'.format(name=self._name))
        app.add_url_rule(
            rule = '/{name}/'.format(name=self._name),
            endpoint=self._name +".index",
            view_func=self.index,
            methods=['GET']
        )

        app.add_url_rule(
            rule = '/{name}/<int:record_id>/'.format(
                name=self._name
            ),
            endpoint=self._name +".edit",
            view_func=self.edit,
            methods=['GET', 'POST']
        )

        app.add_url_rule(
            rule = '/{name}/detail/<int:record_id>/'.format(
                name=self._name
            ),
            endpoint=self._name +".detail",
            view_func=self.detail,
            methods=['GET', 'POST']
        )


        app.add_url_rule(
            rule = '/{name}/add'.format(
                name=self._name
            ),
            endpoint=self._name +".add",
            view_func=self.add,
            methods=['GET', 'POST']
        )

