import pytest
import experiment.hq9p as hq


@pytest.fixture()
def hq9p():
    return hq.hq9p()


def test_hello(capsys, hq9p):
    hq9p.hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello World!\n"


def test_plus(hq9p):
    assert hq9p.var == 0
    hq9p.plus()
    hq9p.plus()
    assert hq9p.var == 2


def test_quine(hq9p, capsys, tmpdir):
    hq9p.action("h")
    hq9p.action("h")
    hq9p.action("9")
    hq9p.action("+")
    hq9p.action("q")
    hq9p.action("q")

    captured = capsys.readouterr()

    assert captured.out.split("\n")[-2] == "hh9+qq"
