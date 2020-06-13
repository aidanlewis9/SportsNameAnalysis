
from collections import defaultdict
from src.parse_data import utils

BABY_NAMES_FILE = 'data/input/baby_names/NationalNames.csv'

def getNameCounts():
    name_counts = defaultdict(lambda: defaultdict(int))

    for row in utils.getRows(BABY_NAMES_FILE):
        if utils.isRecentYear(row['Year']):
            name_counts[row['Gender']][row['Name'].lower()] += int(row['Count'])
    return name_counts

def getGenderCounts(name_counts):
    gender_counts = defaultdict(int)
    for gender in name_counts:
        for name in name_counts[gender]:
            gender_counts[gender] += name_counts[gender][name]
    return gender_counts

def getNamePcts():
    name_counts = getNameCounts()
    gender_counts = getGenderCounts(name_counts)

    name_pcts = dict()

    for gender in name_counts:
        for name in name_counts[gender]:
            name_pcts[name] = name_counts[gender][name] / float(gender_counts[gender])
    return name_pcts
