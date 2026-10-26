from unittest import TestCase
from unittest import main
from random import gauss

def myabs(n):
    if n>=0:
        return n
    elif n<0:
        return -n
    

class TestAbsFunction(TestCase):
    def test_positive_number(self):
        self.assertEqual(myabs(10), 10)

    def test_negative_number(self):
        self.assertEqual(myabs(-10), 10)

    def test_zero(self):
       self.assertEqual(myabs(0), 0)

    def test_random(self):   
        N=1000000
        for i in range(N):
            n=gauss()
            self.assertEqual(myabs(n), abs(n))

main()