from experiment.main import *


def test_hi():
    assert "hi" == return_hi()


def test_hello():
    assert "hello" == return_hello()


def test_fib():
    res = [i for i in fib(10)]
    expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert res == expected
