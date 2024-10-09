import random

def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        input('Press Enter to roll the dice...')
        result = roll_dice()
        print(f'You rolled the dice: {result}!')

        user_input = input('Wanna roll the dice again? (Y/N): ').strip().upper()
        if user_input != 'Y':
            break 

if __name__ == "__main__":
    main()
