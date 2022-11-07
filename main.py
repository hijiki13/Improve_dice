from random import randint
from time import sleep
from datetime import datetime
# Кубик
class Log():
    def __init__(self, log_type, log_msg):
        self.log_type = log_type
        self.log_msg = log_msg
        self.time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    def __str__(self):
        return f'{self.time} - {self.log_type} - {self.log_msg}\n'

def str_center(*strings):
    for i in strings:
        print(i.center(55))
    print()

def bet_play(logs):
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
    
    try:
        while True:
            bet_n = input('You bet on (number): ')
            bet_p = input('Your bet is (points): ')
            print()

            if bet_p.isdigit() and bet_n.isdigit():
                bet_p, bet_n = int(bet_p), int(bet_n)
            
                if bet_n not in range(1, 7):
                    str_center('Invalid bet (not in range 1-6)')

                    log_entry = Log('Error', 'Invalid bet number')
                    logs.write(str(log_entry))
                    continue 
                elif bet_p > score:
                    str_center("Can't bet more points then you have.")

                    log_entry = Log('Error', 'Invalid bet size')
                    logs.write(str(log_entry))
                    continue    
            
                num = randint(1,6)
                sleep(.5)
                str_center(*dice[num])
                if num == bet_n:
                    score += 3*bet_p
                    str_center(f'You got {num}! You win!', f'~~~~~~~SCORE~~~~~~~', f'{score}')
                    log_entry = Log('Info', f'WIN with bet on {bet_n} - Number: {num}')
                    logs.write(str(log_entry))
                else:
                    score -= bet_p
                    str_center(f'You got {num}! Try again!', '~~~~~~~SCORE~~~~~~~', f'{score}')
                    log_entry = Log('Info', f'LOST with bet on {bet_n} - Number: {num}')
                    logs.write(str(log_entry))
                if score < 1:
                    str_center('Sorry, you have no more points!')
                    log_entry = Log('Event', 'Program ended (no points)')
                    logs.write(str(log_entry))
                    return
        
                str_center('Go again?', '(Enter - continue; Q - exit)')
                roll = input()        
                if roll:
                    str_center('~~~~~~GOODBYE!~~~~~~')

                    log_entry = Log("Event", "Program ended (User's choice)")
                    logs.write(str(log_entry))
                    return   
            else:
                str_center('Can be only numbers!')

                log_entry = Log('Error', 'Invalid input')
                logs.write(str(log_entry))
    except KeyboardInterrupt:
        print('\nYou pressed ctrl+c. Program will now end.')
        log_entry = Log('Error', 'KeyboardInterrupt')
        logs.write(str(log_entry))
        log_entry = Log('Event', 'Program ends (Error)')
        logs.write(str(log_entry))
    except Exception as err:
        print('\nUnknown error. Check logs for more information.')
        log_entry = Log('Error', f'{type(err).__name__}')
        logs.write(str(log_entry))
        log_entry = Log('Event', 'Program ends (Error)')
        logs.write(str(log_entry))

def logs():
    with open('logs.txt', 'a') as log:
        log_entry = Log('Event', 'Program starts')
        log.write(str(log_entry))
        bet_play(log)
        log.write('\n')

def read_logs():
    with open('logs.txt', 'r') as log:
        log_data = log.read().split('\n\n')
        log_data.pop()
        total_num = log_data[-1].count('- Info -')
        total = f"Dice rolled {total_num} times"
        won_num = log_data[-1].count('WIN')
        won = f"Won {won_num} times"
        if total_num > 0:
            percent = f'Winning percentage: {(won_num/total_num*100):.2f}%'
            str_center(total, won, percent)
        else:
            str_center("You didn't play")
        
def main():
    logs()
    str_center('Show logs? (Enter)')
    if not input():
        read_logs()

if __name__ == '__main__':
    main()