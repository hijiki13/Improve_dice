from random import randint

def str_center(width=None, *strings):
    if width is None:
        width = 50
    print()
    for i in strings:
        print(i.center(width))
    print()

# Кубик
def bet_play():
    score = 500
    str_center(60, "Let's play!\U0001F3B2", 'You have 500 points!')
    
    while score > 0:
        bet_p = input('Your bet is (points): ')
        bet_n = input('You bet on (number): ')

        if bet_p.isdigit() and bet_n.isdigit():
            bet_p, bet_n = int(bet_p), int(bet_n)
            
            if bet_p > score:
                str_center(60, "Can't bet more points then you have.")
                continue
            elif bet_n not in range(1, 7):
                str_center(60, 'Invalid bet (not in range 1-6)')
                continue       
            
            num = randint(1,6)
            if num == bet_n:
                score += 3*bet_p
                str_center(60, f'You got {num}! You win!', f'~~~~~~~SCORE~~~~~~~', f'{score}')
            else:
                score -= bet_p
                str_center(60, f'You got {num}! Try again!', '~~~~~~~SCORE~~~~~~~', f'{score}')

            roll = input('Go again? (Enter - continue; Q - exit)')        
            if roll:
                str_center(60, 'Goodbye!')
                break
            
        else:
            str_center(60, 'Can be only numbers!')
    str_center(60, 'Sorry, you have no more points!')

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

bet_play()