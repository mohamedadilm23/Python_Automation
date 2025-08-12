# Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
#Method name should have sense
# -k stands for method names execution, -s logs in out put -v stands for more info metadata
#you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail
#fixtures are used as setup and tear down methods for test cases- conftest file to generaliz
#fixture and make it available to all test cases



def test_firstprogram():
 msg="hello"
 assert msg =="this is pytest code startwith hypen otherwise testwill be failed"


def test_secondprogram():
    print("Bye")


def test_thirdprogram():
    print("Hi")

def test_creditcardiob():
        a = 100
        b = 300
        assert a - 2 == 9, "subraction does not match"