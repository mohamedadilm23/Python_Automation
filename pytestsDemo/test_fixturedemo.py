import pytest
@pytest.mark.usefixtures("setup")
class Testexample:

    def test_usecase_parent(self):
     print("I will be excecuting fixture demo method")


    def test_usecase_child(self):
     print("I will be excecuting fixture demo method")

    def test_usecase2(self):
     print("I will be excecuting fixture demo method")

    def test_usecase3(self):
     print("I will be excecuting fixture demo method")

    def test_usecase4(self):
     print("I will be excecuting fixture demo method")

    def test_usecase5(self):
     print("I will be excecuting fixture demo method")

    def test_usecase6(self):
     print("I will be excecuting fixture demo method")