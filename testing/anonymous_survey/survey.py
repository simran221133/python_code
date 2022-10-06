class AnonymousSurvey:

    '''Class for collecting survey anonymously'''
    def __init__(self, question):
        '''Store a question and prepare for user's response'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''Print the question from the user'''
        print(f"{self.question}")

    def store_response(self, new_response):
        '''Get response from the user for the survey'''
        self.responses.append(new_response)

    def show_result(self):
        '''Print response from the user'''
        print("Languages that user speaks: ")
        for response in self.responses:
            print(f"{response.title()}")