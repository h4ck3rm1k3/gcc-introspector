nosetest:
	PYTHONPATH=.	~/experiments/introspector/p34/bin/nosetests 
	# --verbosity=99

test2:
	PYTHONPATH=.	~/experiments/introspector/p34/bin/python3 tests/001_parse_treedef_test.py
