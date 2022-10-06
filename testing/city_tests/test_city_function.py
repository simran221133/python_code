import unittest
from city_function import get_city

class CityTestCase(unittest.TestCase):

    '''Class for testing city test cases'''

    def test_city_country(self):

        '''Method to test the city and country name '''

        formatted_city = get_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):

        '''Method to test the city and country name '''

        formatted_city = get_city('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city, 'Santiago, Chile - Population 5000000')    
    

# if this program is ran unittest.main is run
if __name__ == '__main__':
    unittest.main()