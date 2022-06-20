import random

R = 'камень'
S = 'ножницы'
P = 'бумага'
values = [R, S, P]
continue_game = True
while continue_game:

    player_choice = input('Введите название ')
    comp = random.choice(values)
    print(comp + ' - это выбор компьютера')
    if player_choice == comp:
        result = 'Ничья!'
    elif player_choice == R and comp == S:
        result = 'Вы выйграли!'
    elif player_choice == S and comp == P:
        result = 'Вы выйграли!'
    elif player_choice == P and comp == R:
        result = 'Вы выйграли!'
    else:
        result = 'Увы! Вы проиграли!'
    continue_game = input(f'{result} Если хотите сыграть еще - введите Yes. Если нет - введите No ') == 'Yes'
    if continue_game == False:
        print('Спасибо за игру')


