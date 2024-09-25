import random

guess_number = random.randint(1, 100)
while True:
    try:
        Number = int(input('Guess the number between 1 and 100: '))

        if Number < guess_number:
            print('Too low!')
        elif Number > guess_number:
            print('Too high!')
        else:
            print('Congratulations! You guessed the number.')
            break

    except ValueError:
        print('Please enter a valid number')
