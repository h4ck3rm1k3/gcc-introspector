GNU Compiler Collection introspection in python

a tree node micro service


Goal
====
The goal is to be able to parse out the types of nodes directly from the gcc
without having a copy of the gcc data itself in this project.
We generate python classes to represent the node classes.
Using python dynamic class/type generation.

* add in hints about the class hierarchy.
* parse out the tree dumps into the system.
* dynamically generate python code from gcc tree dump
* interpret and execute gcc tree dumps

Install
=======

uses my branch of the c preprocessor
https://sourceforge.net/u/mdupont/cpip/ci/default/tree/
