#SDEV_220_M05_ProgrammingAssn_Testing
#Tracie Lindquist
#Real Python Getting Started With Testing
#Create the first test case


#import uinttest module
import unittest
from fractions import Fraction

#import sum()
from my_sum import sum

#create the Test class
class TestSum(unittest.TestCase):
    def test_list_init(self):
        """Test to see if __init__ can sum a list of integers"""
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result,6)

#add test case
    def test_list_fraction(self):
        """Test that it can sum a list of fractions"""
        data = [Fraction(1,4), Fraction (1,4), Fraction(2,5)]
        result = sum(data)
        self.assertEqual(result,1)
        print(result)

if __name__ == "__main__":
    unittest.main

#Results discussion:
#In this test case, the first test passes, because 1+2+3 = 6.
#In the command line, I recieved a message that said 1 test ran in less than a second. 
#The second test will NOT pass because 1/4 + 1/4 + 2/5 = 9/10 
#In the command  line I received a message that said two tests ran in .002 seconds and the following message appeared: 
#Traceback (most recent call last):
#  File "C:\Users\traci\Documents\IvyTech\SDEV220\M05\SDEV220_10P_M05_ProgrammingAssn_Testing\test.py", line 27, in test_list_fraction
#    self.assertEqual(result,1)
#AssertionError: Fraction(9, 10) != 1



