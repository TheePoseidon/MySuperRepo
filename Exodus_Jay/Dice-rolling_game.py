import random

while True:
    Trial = input('Roll the dice? (y,n): ').lower()
    if Trial == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif Trial == 'n':
        print('Thank you for playing!')
        break
    else:
        print('Invalid choice!')

