import random
from typing import List


def roll_dice(amount: int = 2) -> List[int]:
    if amount <= 0:
        raise ValueError

    rolls: List[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    total: int = sum(rolls)

    return rolls, total


def main():
    while True:
        try:
            user_input: str = input('How many dice would you like to roll ' )

            if user_input.lower() == 'exit':
                print('Thanks for playing')
                break
            rolls, total = roll_dice(int(user_input))
            print(*rolls, sep=', ')
            print(f'Total: {total}\n')
            #print(*roll_dice(int(user_input)), sep= ', ')
        except ValueError:
            print('Please enter a valid number')

if __name__ == '__main__':
    main()