
from collections import defaultdict
from src.parse_data import utils

NAME_CONVERSIONS_FILE = 'data/input/name_conversions/name_conversions.csv'

def getNicknameToFormalNameMap(baby_name_pcts):
    name_conversions = dict()

    for line in map(str.strip, open(NAME_CONVERSIONS_FILE).readlines()[1:]):
        nickname = utils.getField(line, 0).lower()
        names = map(str.lower, utils.getFields(line, 1))

        popular_name = None
        highest_pct = 0
        for name in names:
            if name in baby_name_pcts and highest_pct <= baby_name_pcts[name]:
                popular_name = name
                highest_pct = baby_name_pcts[name]
        name_conversions[nickname] = popular_name
    return name_conversions
