import random

print('Bienvenido, vamos a jugar piedra, papel o tijera')

def elections():
    options = ('piedra', 'papel', 'tijera')
    
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    if user_option not in options:
      print('esa opcion no es valida')
      print(' ' * 10)
      #continue
      return None, None

    computer_option = random.choice(options)

    print('Computer option =>', computer_option)
    print(' ' * 10)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate!')
        print('*' * 10)
    
    elif user_option == 'piedra' and computer_option == 'tijera' or user_option == 'papel' and computer_option == 'piedra' or user_option == 'tijera' and computer_option == 'papel':
        print(f'Ganas, {user_option} le gana a {computer_option}')
        print('*' * 10)
        user_wins += 1
    
    else:
        print(f'Pierdes, {computer_option} le gana a {user_option}')
        print('*' * 10)
        computer_wins += 1

    return user_wins, computer_wins

def def_wins(user_wins, computer_wins):
    if computer_wins == 2:
        print('El ganador es la computadora')
        return False

    if user_wins == 2:
        print('Eres el ganador')
        return False

    return True

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print(' ' * 10)
        print('ROUND', rounds)
        print(' ' * 10)
    
        print('computer_wins', computer_wins)
        print('user_wins', user_wins)
        print(' ' * 10)
        rounds += 1
    
        user_option, computer_option = elections()
        if user_option is None:
            continue
            
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        
        if not def_wins(user_wins, computer_wins):
            break

run_game()

