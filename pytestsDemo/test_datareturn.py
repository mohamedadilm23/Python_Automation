import pytest
@pytest.mark.usefixtures("dataload")
class TestUsecase2:

 def test_editprofile(self, dataload):
    print(dataload)
    print(dataload[1])

def test_browser_launch(crossbrowser):
    print(f"Running test on: {crossbrowser}")

