
from src.parse_data import baby_names
from src.parse_data import nba
from src.parse_data import name_conversions
from src.analysis import utils

from collections import defaultdict

MALE = 'M'

def getRelativePcts(baby_name_pcts, sport_name_pcts):
    relative_pcts = dict()

    for name in sport_name_pcts:
        if name in baby_name_pcts:
            relative_pcts[name] = sport_name_pcts[name] / baby_name_pcts[name]
    return relative_pcts

def getNonSportNames(baby_name_counts, baby_name_pcts, sport_name_counts):
    non_sport_names = dict()

    for name in baby_name_counts[MALE]:
        if name not in sport_name_counts:
            non_sport_names[name] = baby_name_pcts[name]
    return non_sport_names

def analyzeSportNames(sport, file_prefix, name_conversions, baby_name_counts, baby_name_pcts):
    sport_name_counts = sport.getNameCounts(name_conversions)
    sport_name_pcts = sport.getNamePcts(name_conversions)

    relative_pcts = getRelativePcts(baby_name_pcts, sport_name_pcts)
    utils.writeGoodNamesToCsv(file_prefix, relative_pcts, sport_name_counts)

    non_sport_names = getNonSportNames(baby_name_counts, baby_name_pcts,
        sport_name_counts)
    utils.writeBadNamesToCsv(file_prefix, non_sport_names)

if __name__ == "__main__":
    baby_name_counts = baby_names.getNameCounts()
    baby_name_pcts = baby_names.getNamePcts()
    name_conversions = name_conversions.getNicknameToFormalNameMap(baby_name_pcts)

    analyzeSportNames(nba, "nba", name_conversions, baby_name_counts, baby_name_pcts)
