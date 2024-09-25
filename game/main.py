import random

def display_welcome():
    print('Bienvenido, vamos a jugar piedra, papel o tijera')

def get_user_option():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('Elige: piedra, papel o tijera => ').lower()
    
    while user_option not in options:
        print('Esa opción no es válida. Inténtalo de nuevo.')
        user_option = input('Elige: piedra, papel o tijera => ').lower()
    
    return user_option

def elections():
    user_option = get_user_option()
    computer_option = random.choice(['piedra', 'papel', 'tijera'])
    print(f'Opción de la computadora: {computer_option}')
    return user_option, computer_option

def check_winner(user_option, computer_option):
    if user_option == computer_option:
        return 'empate', None

    wins = {
        'piedra': 'tijera',
        'papel': 'piedra',
        'tijera': 'papel'
    }

    if wins[user_option] == computer_option:
        return 'usuario', user_option
    else:
        return 'computadora', computer_option

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    
    display_welcome()

    while True:
        print(f'\nROUND {rounds}')
        print(f'Victorias - Usuario: {user_wins}, Computadora: {computer_wins}')
        
        user_option, computer_option = elections()
        
        winner, winning_option = check_winner(user_option, computer_option)
        
        if winner == 'empate':
            print('¡Empate!')
        elif winner == 'usuario':
            print(f'¡Ganas! {user_option} le gana a {computer_option}.')
            user_wins += 1
        else:
            print(f'¡Pierdes! {computer_option} le gana a {user_option}.')
            computer_wins += 1
        
        if user_wins == 2 or computer_wins == 2:
            break
        
        rounds += 1

    if user_wins == 2:
        print('¡Eres el ganador!')
    else:
        print('El ganador es la computadora.')

run_game()