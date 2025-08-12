# Any pytest file should start with test or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
import pytest


def test_flower():
    print("Hello Adil how are u")


def test_creditcard():
    a=100
    b=300
    assert a+2==9 ,"Addition does not match"


def test_creditcard2():
    a=100
    b=300
    assert a+2==9 ,"Addition does not match"

@pytest.mark.smoke
def test_flower2():
    print("Hello flower2 how are u")


def test_flower3():
    print("Hello flower3 how are u")

@pytest.mark.skip
def test_flower4():
    print("Hello flower4 how are u")

@pytest.mark.xfail
def test_flower5():
    print("Hello flower5 how are u")

# test_example.py
def test_user_name():
    print("does not match")



def test_user_name():
    print("match")

def test_user_name():
    print("match")

