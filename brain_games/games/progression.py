import random


DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10

def get_question_and_answer():
    startn = random.randint(1, 100)
    step = random.randint(1,30)
    random_index = random.randint(0, PROGRESSION_LENGTH - 1)
    result_list = [
        startn + step * i for i in range(PROGRESSION_LENGTH)
    ]
    answer = result_list[random_index]
    result_list[random_index] = '..'
    question = ' '.join(map(str, result_list))

    return question, answer