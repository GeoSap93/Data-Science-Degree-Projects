import requests
import random

# Fetch data from the API
response = requests.get('https://opentdb.com/api.php?amount=10&category=31')

# Check if the request was successful
if response.status_code != 200:
    print("Failed to fetch questions")
else:
    data = response.json()
    def format_questions(api_data):
        questions = []
        for item in api_data['results']:
            question = {
                'question': item['question'],
                'options': item['incorrect_answers'] + [item['correct_answer']],
                'correct_answer': item['correct_answer']
            }
            random.shuffle(question['options'])
            questions.append(question)
        return questions

    def console_questions(questions):
        correct = []
        incorrect = []

        for question in questions:
            print(question['question'])
            for option in question['options']:
                print(option)

            answer = input('Your answer: ')
            if answer == question['correct_answer']:
                correct.append(question['question'])
            else:
                incorrect.append(question['question'])

        return correct, incorrect

    questions = format_questions(data)
    correct, incorrect = console_questions(questions)

    print(f'You had {len(correct)} correct answers')
    print(f'You had {len(incorrect)} incorrect answers')
