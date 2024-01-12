# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 2024

@author: armin
"""

import random


print(f"{' WELCOME TO BIERWIEGEN ':-^45}\n")

# standard options
options = {'min_drink': 10, 
           'max_drink': 100,
           'shots_int': 3}

player_count = 0

# set up game
game_data = {}
game_data.update({'player_names': []})  # name
game_data.update({'points': []})  # points of every round
game_data.update({'game_won': []})  # if the game was won for every round
game_data.update({'shots_score': []})  # how many victories for shots
game_data.update({'drink_weight': []})  # weight of the drink

# round counter
n = 0
while True:
    # actions
    print('n: next round')
    print('o: change options')
    print('s: show score board')
    print('x: end the game')
    action = input('-> ')
    print('\n')
    
    if action == 'n':
        # set up new game before start
        if n == 0:
            game_data = {}
            game_data.update({'player_names': []})  # name
            game_data.update({'points': []})  # points of every round
            game_data.update({'game_won': []})  # if the game was won for every round
            game_data.update({'shots_score': []})  # how many victories for shots
            game_data.update({'drink_weight': []})  # weight of the drink
                
            # number of players
            while True:
                try:
                    player_count = int(input('How many players are there?\n'))
                    
                    if player_count < 1:
                        raise Exception
                    break
                except ValueError:
                    print('Number of players must be a interger!\n')
                except Exception:
                    print('There must be at least 1 player!\n')
                
            

            for i in range(player_count):
                player_name = input(f'What is the name of player{i+1}?\n')
                game_data.get('player_names').append(player_name)
                game_data.get('points').append([])
                game_data.get('game_won').append([])
                game_data.get('shots_score').append(0)  # how many victories for shots
                
            # weight of drinks
            print('Grap some beer and please start weighing them!')
            for i in range(player_count):
                player_name = game_data.get('player_names')[i]
                while True:
                    try:
                        drink_weight = int(input(f"How much does {player_name}'s drink weigh?\n"))
                        game_data.get('drink_weight').append(drink_weight)
                        break
                    except ValueError:
                        print('Weights must be integers!\n')
                        
            # start of game
            print('Ready to play!\n')
        
        # new beer check
        elif n > 0:
            while True:
                try:
                    new_beer = input('Does anyone have a new beer? [y/n]\n')
                    if new_beer == 'y':
                        new_beer_player = input(f'Who got a new beer? \n')
                        
                        # check if name exists
                        
                        # new beer weight
                        new_beer_weight = int(input(f"How much does {new_beer_player}'s drink weigh?\n"))
                        
                        # index of new beer player
                        new_beer_i = game_data.get('player_names').index(new_beer_player)
        
                        # update drink weight
                        game_data.get('drink_weight')[new_beer_i] = new_beer_weight
                        
                    elif new_beer == 'n':
                        break
                    else:
                        print('Please enter only [y/n]!\n')
                except ValueError:
                    print('Number of players must be a interger!\n')
                    
        n += 1
        print(f"{f' ROUND {n} ':-^45}")
        
        # horizontal line
        print(((player_count + 1) * 15 + 1) * '-')
        
        # how much beer is left
        print(('|{:^14}|' + player_count * '{:^14}|').format(
            'Players', *game_data.get('player_names')
            ))
        print(('|{:^14}|' + player_count * '{:^14}|').format(
            'Drink left', *game_data.get('drink_weight')
            ))
        print(('|{:^14}|' + player_count * '{:^14}|').format(
            'Shot Points', *game_data.get('shots_score')
            ))
        
        # horizontal line
        print(((player_count + 1) * 15 + 1) * '-')
        
        # random number
        drink = random.randint(
            options.get('min_drink'),
            options.get('max_drink'),
            )
        print(f'Drink {drink}! CHEERS!\n')
        
        # reweight of drinks
        drink_dif_list = []
        point_list = []
        
        for i in range(player_count):
            player_name = game_data.get('player_names')[i]
            while True:
                try:
                    old_weight = game_data.get('drink_weight')[i]
                    drink_weight = int(input(f"How much does {player_name}'s drink weigh?\n"))
                    drink_dif = old_weight - drink_weight
                    
                    # check if more
                    if drink_dif < 0:
                        print('You got more than before? There must be something wrong!')
                        continue
                    
                    drink_dif_list.append(drink_dif)
                    
                    points = drink_dif - drink
                    
                    # double points if player drank too little
                    if points < 0:
                        points *= -2
                    point_list.append(points)
                    game_data.get('points')[i].append(points)
                                  
                    # update drink weight
                    game_data.get('drink_weight')[i] = drink_weight
                                                           
                    break
                except ValueError:
                    print('Weights must be integers!\n')
        
        # winner
        winners_i = [i for i, e in enumerate(point_list) if e == min(point_list)]
        
        if len(winners_i) == 1:
            winner_i = winners_i[0]
            winner_name = game_data.get('player_names')[winner_i]
        else:
            winner_names = []
            for winner_i in winners_i:
                winner_names.append(game_data.get('player_names')[winner_i])
            
            print(('We have a tie between' + len(winner_names) * ' {} &').format(*winner_names)[:-2] + '!')
            winner_name = input('Who gets the point?\n')
            winner_i = game_data.get('player_names').index(winner_name)
        
        # score of round
        print('\nSCORES')
        
        # horizontal line
        print(((player_count + 1) * 15 + 1) * '-')
        
        # how much was drunk
        print(('|{:^14}|' + player_count * '{:^14}|').format(
            'Players', *game_data.get('player_names')
            ))
        print(('|{:^14}|' + player_count * '{:^14}|').format(
            'drunk', *drink_dif_list
            ))
        print(('|{:^14}|' + player_count * '{:^14}|').format(
            'Score', *point_list
            ))
        
        # horizontal line
        print(((player_count + 1) * 15 + 1) * '-')
        
        # enter win
        for i in range(player_count):           
            if i == winner_i:
                if point_list[winner_i] == 0:
                    game_data.get('game_won')[i].append(2)
                    game_data.get('shots_score')[i] += 2
                else:
                    game_data.get('game_won')[i].append(1)
                    game_data.get('shots_score')[i] += 1
            else:
                game_data.get('game_won')[i].append(0)
        
        if point_list[winner_i] == 0:
            print(f'\n{winner_name} was PERFECT and has won!\n')
        else:
            print(f'\n{winner_name} has won!\n')
        
        # shots check
        while game_data.get('shots_score')[winner_i] >= options.get('shots_int'):
            print('SHOT! SHOT! SHOT APPARAT!')
            print(f'{winner_name} can hand out shots!\n')
            game_data.get('shots_score')[winner_i] -= options.get('shots_int')
        
    # score board
    elif action == 's':
        print(f"{' SCOREBOARD ':-^45}")
        
        # horizontal line
        print(((player_count + 1) * 15 + 1) * '-')
        
        # table head
        print(('|{:^14}|' + player_count * '{:^14}|').format(
            'Players', *game_data.get('player_names')
            ))
        
        # rounds score
        for r in range(n):
            print(('|{:^14}|' + player_count * '{:^14}|').format(
                f'ROUND{r+1}', *[x[r] for x in game_data.get('points')]
                ))
        
        # horizontal line
        print(((player_count + 1) * 15 + 1) * '-')
        
        # sum
        print(('|{:^14}|' + player_count * '{:^14}|').format(
            'SUM', *[sum(x) for x in game_data.get('points')]
            ))
        
        # horizontal line
        print(((player_count + 1) * 15 + 1) * '-')
        
        # won games
        print(('|{:^14}|' + player_count * '{:^14}|').format(
            'VICTORIES', *[sum(x) for x in game_data.get('game_won')]
            ))
        
        # horizontal line
        print(((player_count + 1) * 15 + 1) * '-')
        
        print('\n')
    
    # options
    elif action == 'o':
        while True:
            try:
                print('Please select the game options!')
                min_drink = int(input('Min drinking weight\n'))
                max_drink = int(input('Max drinking weight\n'))
                shots_int = int(input('After how many wins are you allowed to give out shots?\n'))
                options = {'min_drink': min_drink, 
                           'max_drink': max_drink,
                           'shots_int': shots_int}
                
                if min_drink > max_drink:
                    raise Exception
                print('\n')
                break
            except ValueError:
                print('All options must be integers!\n')
            except Exception:
                print('Min drink weight is higher than max drink weight!\n')
    
    # exit the game
    elif action == 'x':
        break
    
print(f"{' GOODBYE ':-^45}")
