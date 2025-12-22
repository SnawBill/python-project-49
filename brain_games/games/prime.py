import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = random.randint(1, 1000)
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1
    question = number
    answer = 'yes' if counter == 2 else 'no'
    return question, answer