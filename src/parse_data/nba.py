
from collections import defaultdict

from src.parse_data import utils

NBA_PLAYERS_FILE = 'data/input/nba_players/all_seasons.csv'

def getUniqueId(row):
    return "|".join([row['player_name'], row['country'],
           row['draft_year'], row['draft_round'], row['draft_number']])

def getUniquePlayers(rows):
    unique_rows = list()
    unique_ids = set()

    for row in rows:
        unique_id = getUniqueId(row)
        if unique_id not in unique_ids:
            unique_rows.append(row)
            unique_ids.add(unique_id)
    return unique_rows

def getNameCounts(name_conversions):
    player_count = 0
    name_counts = defaultdict(int)

    players = getUniquePlayers(utils.getRows(NBA_PLAYERS_FILE))
    for player in players:
        first_name = utils.getFirstName(player['player_name']).lower()
        formal_name = utils.getFormalName(name_conversions, first_name)

        if utils.isAmerican(player['country']):
            name_counts[formal_name] += 1
    return name_counts

def getTotalPlayerCount(name_counts):
    return sum(v for v in name_counts.values())


def getNamePcts(name_conversions):
    name_counts = getNameCounts(name_conversions)
    player_count = getTotalPlayerCount(name_counts)
    name_pcts = dict()

    for name in name_counts:
        if utils.isSignificant(name_counts[name]):
            name_pcts[name] = name_counts[name] / float(player_count)
    return name_pcts
