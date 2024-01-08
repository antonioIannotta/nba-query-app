from time import sleep
import os
import pandas as pd

import requests

PLAYERS_URL = "https://www.balldontlie.io/api/v1/players"
PLAYERS_PAGES_NUMBER = 209
PLAYERS_FILE_PATH = "../backend/players.csv"


def update_player_db():
    players_dataframe = pd.DataFrame(columns=['first_name', 'last_name', 'position', 'team_name', 'team_city',
                                              'team_abbr', 'team_conference', 'team_division'])

    first_name = []
    last_name = []
    position = []
    team_name = []
    team_city = []
    team_abbr = []
    team_conference = []
    team_division = []
    for page in range(0, PLAYERS_PAGES_NUMBER):
        response: requests.Response = requests.get(PLAYERS_URL, params={'page': page, 'per_page': 100})
        if response.status_code == 200:
            for player_json in response.json()['data']:
                first_name.append(player_json['first_name'])
                last_name.append(player_json['last_name'])
                position.append(player_json['position'])
                team_name.append(player_json['team']['full_name'])
                team_city.append(player_json['team']['city'])
                team_abbr.append(player_json['team']['abbreviation'])
                team_conference.append(player_json['team']['conference'])
                team_division.append(player_json['team']['division'])
        else:
            print(f"Error: {response.status_code}")
            exit()
        sleep(2)
    players_dataframe['first_name'] = first_name
    players_dataframe['last_name'] = last_name
    players_dataframe['position'] = position
    players_dataframe['team_name'] = team_name
    players_dataframe['team_city'] = team_city
    players_dataframe['team_abbr'] = team_abbr
    players_dataframe['team_conference'] = team_conference
    players_dataframe['team_division'] = team_division
    players_dataframe.to_csv(PLAYERS_FILE_PATH, index=False)

