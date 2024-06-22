from random import choice
#choice picks a random element


def run_game():
    # Assign a list of three different words to word which is a string
    word: str = choice(['apple', 'secret', 'banana'])

    user: str = input('What is your name?>> ')
    print(f'Welcome to Hangman, {user}!')

    #Setup tries
    guessed: str = ''
    tries: int = 3

    while tries > 0:
        blanks: int = 0

        print('Word ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end = '')
                blanks =+ 1

        print() # adds a blank line

        if blanks == 0:
            print('You got it!')
            break

        while True:
            guess: str = input('Enter a letter: ')
            if len(guess) > 1:
                print(f'Too many characters. Only enter one letter at a time')
                continue
            else:
                break

        if guess in guessed:
            print(f'You already used: "{guess}" Please use a different letter')
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Sorry, incorrect...({tries} tries remaining)')

            if tries == 0:
                print('No more tries remaining. You lose')
                break

if __name__ == '__main__':
    run_game()