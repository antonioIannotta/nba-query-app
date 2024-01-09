import pandas as pd
import requests

TEAMS_URL = "https://www.balldontlie.io/api/v1/teams"
TEAMS_FILE_PATH = "../backend/teams.csv"

def teams_db():
    teams_dataframe = pd.DataFrame(columns=['name', 'full_name', 'abbreviation', 'city', 'conference', 'division'])

    name = []
    full_name = []
    abbreviation = []
    city = []
    conference = []
    division = []

    for team_index in range(0, 30):
        response: requests.Response = requests.get(TEAMS_URL)
        if response.status_code == 200:
            team_json = response.json()['data'][team_index]
            name.append(team_json['name'])
            full_name.append(team_json['full_name'])
            abbreviation.append(team_json['abbreviation'])
            city.append(team_json['city'])
            conference.append(team_json['conference'])
            division.append(team_json['division'])
        else:
            print(f"Error: {response.status_code}")
            exit()

    teams_dataframe['name'] = name
    teams_dataframe['full_name'] = full_name
    teams_dataframe['abbreviation'] = abbreviation
    teams_dataframe['city'] = city
    teams_dataframe['conference'] = conference
    teams_dataframe['division'] = division

    teams_dataframe.to_csv(TEAMS_FILE_PATH, index=False)