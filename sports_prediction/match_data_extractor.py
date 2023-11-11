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

# response_leagues = requests.get(
#     url=f"{BASE_URL}/leagues",
#     headers={
#         'X-RapidAPI-Key': API_KEY
#     }
# )

# # print(response_leagues.content)

# parsed = json.loads(response_leagues.content)


# TEAMS INFO

league_id = 30 # LALIGA

response_teams = requests.get(
    url=f"{BASE_URL}/teams/league/{league_id}",
    headers={
        'X-RapidAPI-Key': API_KEY
    }
)

parsed_teams = json.loads(response_teams.content)


# TEAMS STATS

team_id_list = [team['team_id'] for team in parsed_teams['api']['teams']]

team_stats = []

for team_id in team_id_list:

    response_stats = requests.get(
        url=f"{BASE_URL}/tstatistics/{league_id}/{team_id}",
        headers={
            'X-RapidAPI-Key': API_KEY
        }
    )

    parsed_stats = json.loads(response_stats.content)
    team_stats.append(parsed_stats)



# partidos jornada actual
# fixtures/rounds/{league_id}/current

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


