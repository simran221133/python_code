from survey import AnonymousSurvey

question = "What language do you speak in?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()

print("Hit 'q' to quit at any time.")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    else:
        my_survey.store_response(response)

print("Thanks for participating in the survey.")
my_survey.show_result()




