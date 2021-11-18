import random
import requests


# defining function pulling pokemon data on character name, id, height and weight from pokemon API
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }


# define function user gets random selection of 3 pokemon to choose from
def run():
    my_pokemon_1 = random_pokemon()
    my_pokemon_2 = random_pokemon()
    my_pokemon_3 = random_pokemon()
    print('You were given {}, {} and {}'.format(my_pokemon_1['name'], my_pokemon_2['name'], my_pokemon_3['name']))

# user selects which pokemon to play the game with
    user_choice = int((input('Which Pokemon will you select to battle? 1, 2 or 3? ')))
    print(user_choice)
    if user_choice == 1:
        user_choice = my_pokemon_1
    elif user_choice == 2:
        user_choice = my_pokemon_2
    elif user_choice == 3:
        user_choice = my_pokemon_3

# user selects which statistic to play with - id, height or weight
    stat_choice = input('Which stat do you want to use to battle? (id, height, weight) ')

# random selection of computer opponent pokemon
    opponent_pokemon1 = random_pokemon()
    opponent_pokemon2 = random_pokemon()
    opponent_pokemon3 = random_pokemon()
    opponent_pokemon = random.randint(0, 2)
    if opponent_pokemon == 0:
        opponent_pokemon = opponent_pokemon1
    elif opponent_pokemon == 1:
        opponent_pokemon = opponent_pokemon2
    elif opponent_pokemon == 2:
        opponent_pokemon = opponent_pokemon3

# print which pokemon characters the computer got (via random generation) and which one selected to play
    print('The opponent got {}, {}, and {}'.format(opponent_pokemon1['name'], opponent_pokemon2['name'],
                                                   opponent_pokemon3['name']))
    print('The opponent chose {}'.format(opponent_pokemon['name']))

# determining whether user or computer wins the game using if/else to compare selected stats
    my_stat = user_choice[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    player_wins = 0
    cpu_wins = 0

    if my_stat > opponent_stat:
        player_wins += 1
        print('You Win!')
        with open('high_scores.txt', 'w+') as text_file:
            win = '1'
            text_file.write(win)
    elif my_stat < opponent_stat:
        cpu_wins += 1
        print('You Lose!')
        with open('high_scores.txt', 'w+') as text_file:
            lose = '0'
            text_file.write(lose)
    else:
        print('Draw!')
    return {'player_wins': player_wins, 'cpu_wins': cpu_wins
            }

# loop to play game again


round_result = run()
print('Player wins {}'.format(round_result['player_wins']))
print('CPU wins {}'.format(round_result['cpu_wins']))
play_again = input('Do you want to play again? (y/n) ')
if play_again == 'y':
    run()
else:
    print('Thanks for playing!')


run()
