import requests

PLAYERS_URL = "https://www.balldontlie.io/api/v1/players"
PLAYERS_PAGES_NUMBER = 209


class Team:
    def __init__(self,
                 abbreviation: str,
                 city: str,
                 conference: str,
                 division: str,
                 team_name: str):
        self.abbreviation = abbreviation
        self.city = city
        self.conference = conference
        self.division = division
        self.team_name = team_name


class Player:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 position: str,
                 team: Team):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.team = team

    def print_player(self):
        print("\nNBA PLAYER CARD")
        print("Player: ", self.first_name + " " + self.last_name)
        print("Position: ", self.position)
        print("Team: ", self.team.team_name)
        print("****************\n")


def get_all_players():
    player_list: list[Player] = []
    response: requests.Response = requests.get(PLAYERS_URL)
    if response.status_code == 200:
        for player_json in response.json()['data']:
            player_list.append(_return_player(player_json))
    else:
        print(f"Error: {response.status_code}")

    return player_list


def _return_player(player_json: dict) -> Player:
    team_dict: dict = player_json['team']
    team_abbreviation: str = team_dict['abbreviation']
    team_city: str = team_dict['city']
    team_conference: str = team_dict['conference']
    team_division: str = team_dict['division']
    team_name: str = team_dict['full_name']

    team: Team = Team(team_abbreviation, team_city, team_conference, team_division, team_name)

    player_name = player_json['first_name']
    player_last_name = player_json['last_name']
    player_position = player_json['position']

    return Player(player_name, player_last_name, player_position, team)

# TODO: return all the players exploiting the page number
