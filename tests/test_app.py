# tests/test_app.py
import app  # assuming your main script is app.py

def test_add():
    assert app.add(2, 3) == 5

def test_divide_by_zero():
    try:
        app.divide(4, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False
