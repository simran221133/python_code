from http.client import responses
from survey import AnonymousSurvey
import unittest

class TestSurvey(unittest.TestCase):
    '''Class for unit testing the survey class'''

    def setUp(self):
        '''special method to store common instance for testing multiple cases'''

        # storing question for the survey
        question = "What language do you speak in?"
        # making instance of AnonymousSurvey with question as input
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Hindi', 'Spanish']

    def test_store_single_response(self):
        '''Method to test storing a single response'''

        # calling store_response method from AnonymousSurvey to store a response
        self.my_survey.store_response(self.responses[0])
        # if 'English' is present in user response
        self.assertIn('English', self.my_survey.responses[0])

    def test_store_three_response(self):
        '''Method to test storing three responses'''

        # storing each response in the list
        for response in self.responses:
            self.my_survey.store_response(response)
            
        # asserting on each response in the list        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
    
        