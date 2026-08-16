from app import add, greet


def test_add():
#    assert add(2, 3) == 5
assert add(2, 3) == 999

def test_greet():
    assert greet("Zeeshan") == "Hello, Zeeshan!"
