from random import randint

lower_num, higher_num = 1, 10
random_number: int = randint(lower_num, higher_num)
print(f'Guess the number from {lower_num} to {higher_num}.')

limit = 0
while True:
    try:
        user_guess: int = int(input('Guess:'))
    except ValueError as e:
        print('Please enter a valid NUMBER')
        continue
    if limit >= 3:
        print(f'Your three guesses are up. The number was {random_number}')
        break
    if user_guess > random_number:
        print('The number is lower')
        print(f'limit is {limit}')
        limit += 1
    elif user_guess < random_number:
        print('The number is higher')
        limit += 1
        print(f'limit is {limit}')
    else:
        print('You guessed it')
        break
