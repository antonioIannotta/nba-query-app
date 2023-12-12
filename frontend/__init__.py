from backend.players import *

player_list = get_all_players()

if not player_list:
    print("Error!")
else:
    for player in player_list:
        player.print_player()

