from survey import AnonymousSurvey
import unittest

class TestSurvey(unittest.TestCase):
    '''Class for unit testing the survey class'''

    def test_store_single_response(self):
        '''Method to test storing a single response'''

        # storing question for the survey
        question = "What language do you speak in?"
        # making instance of AnonymousSurvey with question as input
        my_survey = AnonymousSurvey(question)
        # calling store_response method from AnonymousSurvey to store a response
        my_survey.store_response('English')
        # if 'English' is present in user response
        self.assertIn('English', my_survey.responses)

    def test_store_three_response(self):
        '''Method to test storing three responses'''
        question = "What language do you speak in?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Hindi', 'Spanish']
        my_survey.store_response(responses)
        self.assertIn(responses, my_survey.responses)

if __name__ == '__main__':
    unittest.main()
    
        