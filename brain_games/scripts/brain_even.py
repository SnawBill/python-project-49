import random
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May i have your name? ')
    print(f'Hello, {name}!')
    counter = 0
    for _ in range(3):
        print('''Answer "yes" if the number is even, otherwise answer "no".''')
        random_number = random.randint(1, 100)
        result = ''
        if random_number % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        print(f'Question: {random_number}')
        answer = input('Your answer: ')
        if answer != result:
            print(f''''{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!''')
            break
        else:
            print('Correct!')
            counter += 1
    if counter == 3:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()