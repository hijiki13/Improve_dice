from random import randint
from time import sleep
from datetime import datetime

# класс для записывания логов по одному образцу
class Log():
    def __init__(self, log_type, log_msg):
        self.log_type = log_type
        self.log_msg = log_msg
        self.time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    def __str__(self):
        return f'{self.time} - {self.log_type} - {self.log_msg}\n'
# функция для выравнивания строк по центру
def str_center(*strings):
    for i in strings:
        print(i.center(55))
    print()
# главная функция
def bet_play(logs):
    # словарь для отображения псевдографики
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
    str_center("Сыграем!\U0001F3B2", 'У Вас 500 очков.')
    
    try:
        while True:
            bet_n = input('Ваша ставка (число): ')
            bet_p = input('Сколько ставите очков: ')
            print()

            if bet_p.isdigit() and bet_n.isdigit():
                bet_p, bet_n = int(bet_p), int(bet_n)

                # проверка вводимых данных
                if bet_n not in range(1, 7):
                    str_center('Недействительное число. Должно быть в промежутке 1-6.')

                    log_entry = Log('Error', 'Invalid bet number') 
                    logs.write(str(log_entry)) #запись в логи
                    continue 
                elif bet_p > score:
                    str_center("Нельзя поставить больше очков, чем у Вас есть.")

                    log_entry = Log('Error', 'Invalid bet size')
                    logs.write(str(log_entry))
                    continue    
            
                # бросается кубик, показывается результат
                num = randint(1,6)
                sleep(.3)
                str_center(*dice[num])
                if num == bet_n:
                    score += 3*bet_p
                    str_center(f'Выпало {num}! Вы выиграли!', f'~~~~~~~СЧЕТ~~~~~~~', f'{score}')
                    log_entry = Log('Info', f'WIN with bet on {bet_n} - Number: {num}')
                    logs.write(str(log_entry))
                else:
                    score -= bet_p
                    str_center(f'Выпало {num}! Попробуйте еще раз!', '~~~~~~~СЧЕТ~~~~~~~', f'{score}')
                    log_entry = Log('Info', f'LOST with bet on {bet_n} - Number: {num}')
                    logs.write(str(log_entry))
                if score < 1:
                    str_center('У Вас закончились очки!')
                    log_entry = Log('Event', 'Program ended (no points)')
                    logs.write(str(log_entry))
                    return
                # Пользователю дается шанс выйти из программы
                str_center('Пропробовать еще раз?', '(Enter - продолжить; Q - выход)')
                roll = input()        
                if roll:
                    str_center('~~~~~~ДО СВИДАНИЯ!~~~~~~')

                    log_entry = Log("Event", "Program ended (User's choice)")
                    logs.write(str(log_entry))
                    return   
            else:
                str_center('Можно вводить только числа.')

                log_entry = Log('Error', 'Invalid input')
                logs.write(str(log_entry))
    # обработка изключений (с записью в логи)
    except KeyboardInterrupt:
        print('\nВы нажали ctrl+c. Выход из программы.')
        log_entry = Log('Error', 'KeyboardInterrupt')
        logs.write(str(log_entry))
        log_entry = Log('Event', 'Program ends (Error)')
        logs.write(str(log_entry))
    except Exception as err:
        print('\nНеизвестная ошибка. Больше информации можно узнать в логах.')
        log_entry = Log('Error', f'{type(err).__name__}')
        logs.write(str(log_entry))
        log_entry = Log('Event', 'Program ends (Error)')
        logs.write(str(log_entry))
# функция для записывания логов
def logs():
    with open('logs.txt', 'a') as log:
        log_entry = Log('Event', 'Program starts')
        log.write(str(log_entry))
        bet_play(log)
        log.write('\n')
# функция для вывода информавции из логов (процент выигрыша)
def read_logs():
    with open('logs.txt', 'r') as log:
        log_data = log.read().split('\n\n')
        log_data.pop()
        total_num = log_data[-1].count('- Info -')
        total = f"Кубик был брошен {total_num} раз;"
        won_num = log_data[-1].count('WIN')
        won = f"Из них {won_num} побед;"
        if total_num > 0:
            percent = f'Процент выигрыша: {(won_num/total_num*100):.2f}%'
            str_center(total, won, percent)
        else:
            str_center("Вы ни разу не кинули кубик.")
        
def main():
    logs()
    str_center('Показать логи? (Enter)')
    if not input():
        read_logs()

if __name__ == '__main__':
    main()