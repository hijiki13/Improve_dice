from random import randint
# Кубик
def bet_play():
    roll = "Let's play! You have 500 points!"
    score = 500
    print(roll)
    while score > 0:
        bet_p = input('Your bet (points): ')
        bet_n = input('Your bet on (number): ')
        if bet_p.isdigit() and bet_n.isdigit():
            bet_p = int(bet_p)
            bet_n = int(bet_n)
            roll = input('Roll it! (Enter)\n')        
            if roll:
                print('Goodbye!')
                break
            num = randint(1,6)
            if num == bet_n:
                score += 3*bet_p
                print(f'You got {num}! You win!\nScore: {score}')
            else:
                score -= bet_p
                print(f'You got {num}! Try again!\nScore: {score}')
        else:
            print('Can be only numbers!')
    else:
        print('Sorry, you have no more points!')
# bet_play()