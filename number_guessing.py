import random 

def game():
    num = random.randint(1, 100)
    attempts_left = 10  
    for _ in range(attempts_left):
        a = float(input('Do you know which number is correct? '))
        
        if a == num:
            print('Congratulations :D')
            break
        elif a > num:
            print('Number greater than chosen')
        elif a < num:
            print('Number smaller than chosen')

        attempts_left -= 1 
        if attempts_left > 0:
            print(f'You have {attempts_left} attempts left.')
        else:
            print('Your attempts are over :( ')
            print(f'The correct number was {num}.')
game()
