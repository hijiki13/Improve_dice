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
def bet_play():
    # начальная запись в логи (программа запущенна)
    logs('Event', 'Program starts')
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
                    logs('Error', 'Invalid bet number') #запись в логи
                    continue 
                elif bet_p > score:
                    str_center("Нельзя поставить больше очков, чем у Вас есть.")
                    logs('Error', 'Invalid bet size')
                    continue    
            
                # бросается кубик, показывается результат
                num = randint(1,6)
                sleep(.3)
                str_center(*dice[num])
                if num == bet_n:
                    score += 3*bet_p
                    str_center(f'Выпало {num}! Вы выиграли!', f'~~~~~~~СЧЕТ~~~~~~~', f'{score}')
                    logs('Info', f'WIN with bet on {bet_n} - Number: {num}')
                else:
                    score -= bet_p
                    str_center(f'Выпало {num}! Попробуйте еще раз!', '~~~~~~~СЧЕТ~~~~~~~', f'{score}')
                    logs('Info', f'LOST with bet on {bet_n} - Number: {num}')
                if score < 1:
                    str_center('У Вас закончились очки!')
                    logs('Event', 'Program ended (no points)')
                    return
                # Пользователю дается шанс выйти из программы
                str_center('Пропробовать еще раз?', '(Enter - продолжить; Q - выход)')
                roll = input()        
                if roll:
                    str_center('~~~~~~ДО СВИДАНИЯ!~~~~~~')
                    logs("Event", "Program ended (User's choice)\n")
                    return   
            else:
                str_center('Можно вводить только числа.')
                logs('Error', 'Invalid input')
    # обработка иcключений (с записью в логи)
    except KeyboardInterrupt:
        print('\nВы нажали ctrl+c. Выход из программы.')
        logs('Error', 'KeyboardInterrupt')
        logs('Event', 'Program ends (Error)\n')
    except Exception as err:
        print('\nНеизвестная ошибка. Больше информации можно узнать в логах.')
        logs('Error', f'{type(err).__name__}')
        logs('Event', 'Program ends (Error)\n')
# функция для записывания логов
def logs(msg_type: str, msg: str):
    with open('logs.txt', 'a') as log:
        log_entry = Log(msg_type, msg)
        log.write(str(log_entry))
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
    bet_play()
    str_center('Показать логи? (Enter)')
    if not input():
        read_logs()

if __name__ == '__main__':
    main()