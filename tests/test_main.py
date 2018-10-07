from experiment.main import return_hi, return_hello

def test_hi():
	assert "hi" == return_hi()

def test_hello():
	assert "hello" == return_hello()
