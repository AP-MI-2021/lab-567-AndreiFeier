from Test.testDomain import testCheltuiala
from Test.testCrud import testAdaugaCheltuiala, testStergeCheltuiala, testModificaCheltuiala
from Test.testFunctionalitati import testOrdonareDupaSuma, testSumaPerApartament


def runAllTests():
    testCheltuiala()
    testAdaugaCheltuiala()
    testStergeCheltuiala()
    testModificaCheltuiala()

    testOrdonareDupaSuma()
    testSumaPerApartament()