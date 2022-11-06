from random import randint
from time import sleep

def str_center(*strings):
    for i in strings:
        print(i.center(55))
    print()

# Кубик
def bet_play():
    dice = {
        1: (
            '┌─────────┐',
            '│         │',
            '│    ●    │',
            '│         │',
            '└─────────┘'
        ),
        2: (
            '┌─────────┐',
            '│ ●       │',
            '│         │',
            '│       ● │',
            '└─────────┘'
        ),
        3: (
            '┌─────────┐',
            '│ ●       │',
            '│    ●    │',
            '│       ● │',
            '└─────────┘'
        ),
        4: (
            '┌─────────┐',
            '│ ●     ● │',
            '│         │',
            '│ ●     ● │',
            '└─────────┘'
        ),
        5: (
            '┌─────────┐',
            '│ ●     ● │',
            '│    ●    │',
            '│ ●     ● │',
            '└─────────┘'
        ),
        6: (
            '┌─────────┐',
            '│ ●     ● │',
            '│ ●     ● │',
            '│ ●     ● │',
            '└─────────┘'
        )
    }

    score = 500
    str_center("Let's play!\U0001F3B2", 'You have 500 points!')
    
    while True:
        bet_n = input('You bet on (number): ')
        bet_p = input('Your bet is (points): ')
        print()

        if bet_p.isdigit() and bet_n.isdigit():
            bet_p, bet_n = int(bet_p), int(bet_n)
            
            if bet_p > score:
                str_center("Can't bet more points then you have.")
                continue
            elif bet_n not in range(1, 7):
                str_center('Invalid bet (not in range 1-6)')
                continue       
            
            num = randint(1,6)
            sleep(.5)
            str_center(*dice[num])
            if num == bet_n:
                score += 3*bet_p
                str_center(f'You got {num}! You win!', f'~~~~~~~SCORE~~~~~~~', f'{score}')
            else:
                score -= bet_p
                str_center(f'You got {num}! Try again!', '~~~~~~~SCORE~~~~~~~', f'{score}')
            
            if score < 1:
                str_center('Sorry, you have no more points!')
                return
        
            str_center('Go again?', '(Enter - continue; Q - exit)')
            roll = input()        
            if roll:
                str_center('Goodbye!')
                return   
        else:
            str_center('Can be only numbers!')
bet_play()