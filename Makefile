
peewee:
	PYTHONPATH=.	~/experiments/introspector/p34/bin/python3 tests/002_peewee_test.py

nosetest:
	PYTHONPATH=.	~/experiments/introspector/p34/bin/nosetests 


test2:
	PYTHONPATH=.	~/experiments/introspector/p34/bin/python3 tests/001_parse_treedef_test.py

start-doc :
	~/experiments/introspector/p34/bin/python3 ../sphinx/sphinx-quickstart.py
