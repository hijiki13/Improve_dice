from random import randint
# Кубик
def bet_play():
    roll = "Let's play!\U0001F3B2 \nYou have 500 points!"
    score = 500
    print(roll)
    while score > 0:
        bet_p = input('Your bet is (points): ')
        bet_n = input('You bet on (number): ')

        if bet_p.isdigit() and bet_n.isdigit():
            bet_p, bet_n = int(bet_p), int(bet_n)
            
            if bet_p > score:
                print("Can't bet more points then you have.")
                continue
            elif bet_n not in range(1, 7):
                print('Invalid bet (not in range 1-6)')
                continue       
            
            num = randint(1,6)
            if num == bet_n:
                score += 3*bet_p
                print(f'You got {num}! You win!\nScore: {score}')
            else:
                score -= bet_p
                print(f'You got {num}! Try again!\nScore: {score}')

            roll = input('Go again? (Enter - continue; Q - exit)\n')        
            if roll:
                print('Goodbye!')
                break
            
        else:
            print('Can be only numbers!')
    else:
        print('Sorry, you have no more points!')

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