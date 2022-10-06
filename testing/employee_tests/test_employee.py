from employee import Employee
import unittest

class TestEmployee(unittest.TestCase):
    '''Class for employee unit tests'''

    def setUp(self):
        '''method for testing on a common instance'''
        self.test_employee = Employee("Rondu", "Singh", 30000)

    def test_give_default_raise(self):
        '''unit test for default raise'''
        self.assertEqual(35000, self.test_employee.give_raise())

    def test_give_custom_raise(self):
        '''unit test for custom raise'''
        self.assertEqual(45000, self.test_employee.give_raise.new_salary)

if __name__ == '__main__':
    unittest.main()


    
