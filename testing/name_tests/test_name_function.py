# import module unittest for writting a unit test
import unittest
# from file 'function' and import get_formatted_name
from function_tc import get_formatted_name

class NameTestCase(unittest.TestCase):

    '''Class for writting the test case'''

    # IMP to start the function name with test, python know automatically to run this method
    # writing a function for the test case with first_name & last_name
    def test_first_last_name_case(self):
 
        # assigning variable 'formatted_name' to call function 'get_formatted_name'
        formatted_name = get_formatted_name('sam', 'kaur')
        # checking if 'value from the function' is equal to the 'expected value'
        self.assertEqual(formatted_name, 'Sam Kaur')
    
    # IMP to start the function name with test, python know automatically to run this method
    # writing a function for the test case with first_name, last_name & middle_name
    def test_first_last_middle_name_case(self):
 
        # assigning variable 'formatted_name' to call function 'get_formatted_name'
        formatted_name = get_formatted_name('sam', 'kaur', 'sweety')
        # checking if 'value from the function' is equal to the 'expected value'
        self.assertEqual(formatted_name, 'Sam Sweety Kaur')

# if the test_name_function is ran 
# unitest.main() is called
if __name__ == '__main__':
    unittest.main()