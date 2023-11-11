import requests
import os                                                                                                                                                                                                          
from dotenv import load_dotenv
import json

# from pathlib import Path
# load_dotenv(Path("/my/path/.env"))

load_dotenv()

print(os.getenv("API_KEY"))

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://v2.api-football.com"

# API STATUS INFO

# response_status = requests.get(
#     url=f"{BASE_URL}/status",
#     headers={
#         'X-RapidAPI-Key': API_KEY
#     }
# )

# print(response_status.content)

# LEAGUES INFO:

# obtener ligas del pais y año
# response_leagues = requests.get(
#     url=f"{BASE_URL}/leagues/country/ES/2023",
#     headers={
#         'X-RapidAPI-Key': API_KEY
#     }
# )

# parsed_seasons = json.loads(response_leagues.content)

# with open('data/parsed_seasons.json', 'w', encoding='utf-8') as f:
#     json.dump(parsed_seasons, f, ensure_ascii=False, indent=4)

# read file
with open('data/parsed_seasons.json', 'r') as myfile:
    data=myfile.read()

# parse file
parsed_seasons = json.loads(data)

# obtener id de la liga temporada actual
# LALIGA
league_id = parsed_seasons['api']['leagues'][0]['league_id']
# league_id = 5284 # LALIGA


# TEAMS INFO

# response_teams = requests.get(
#     url=f"{BASE_URL}/teams/league/{league_id}",
#     headers={
#         'X-RapidAPI-Key': API_KEY
#     }
# )

# parsed_teams = json.loads(response_teams.content)

# with open('data/parsed_teams.json', 'w', encoding='utf-8') as f:
#     json.dump(parsed_teams, f, ensure_ascii=False, indent=4)


# read file
with open('data/parsed_teams.json', 'r') as myfile:
    data=myfile.read()

# parse file
parsed_teams = json.loads(data)


# TEAMS STATS

team_id_list = [team['team_id'] for team in parsed_teams['api']['teams']]

# team_stats = []

# for team_id in team_id_list:

#     response_stats = requests.get(
#         url=f"{BASE_URL}/statistics/{league_id}/{team_id}",
#         headers={
#             'X-RapidAPI-Key': API_KEY
#         }
#     )

#     parsed_stats = json.loads(response_stats.content)
#     team_stats.append({team_id : parsed_stats['api']['statistics']})


# with open('data/team_stats.json', 'w', encoding='utf-8') as f:
#     json.dump(team_stats, f, ensure_ascii=False, indent=4)

# read file
with open('data/team_stats.json', 'r') as myfile:
    data=myfile.read()

# parse file
team_stats = json.loads(data)


# obtener jornada actual de la liga
# fixtures/rounds/{league_id}/current

# response_rounds = requests.get(
#     url=f"{BASE_URL}/fixtures/rounds/{league_id}/current",
#     headers={
#         'X-RapidAPI-Key': API_KEY
#     }
# )

# parsed_rounds = json.loads(response_rounds.content)

# with open('data/parsed_rounds.json', 'w', encoding='utf-8') as f:
#     json.dump(parsed_rounds, f, ensure_ascii=False, indent=4)


# read file
with open('data/parsed_rounds.json', 'r') as myfile:
    data=myfile.read()

# parse file
parsed_rounds = json.loads(data)    

current_round = parsed_rounds['api']['fixtures'][0]

## obtener partidos de la jornada actual
# response_fixtures = requests.get(
#     url=f"{BASE_URL}/fixtures/league/{league_id}/{current_round}",
#     headers={
#         'X-RapidAPI-Key': API_KEY
#     }
# )

# parsed_fixtures = json.loads(response_fixtures.content)

# with open('data/parsed_fixtures.json', 'w', encoding='utf-8') as f:
#     json.dump(parsed_fixtures, f, ensure_ascii=False, indent=4)

# read file
with open('data/parsed_fixtures.json', 'r') as myfile:
    data=myfile.read()

# parse file
parsed_fixtures = json.loads(data)    


fixture_id = 1038076

# obtener odds del partido por id
response_odds = requests.get(
    url=f"{BASE_URL}/odds/fixture/{fixture_id}",
    headers={
        'X-RapidAPI-Key': API_KEY
    }
)

parsed_odds = json.loads(response_odds.content)

# odds jornada actual
# odds/fixture/{fixture_id}

# predicciones
# predictions/{fixture_id}


# logica:
# buscar partidos de la jornada actual
# buscar odds de los partidos
# los odds ente 1.2 y 1.3
# sacar prediccion


print("END")


