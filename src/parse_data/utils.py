import csv

COUNT_THRESHOLD = 1
DEFAULT_DELIMITER = ','
MALE = 'M'
START_YEAR = 1980
USA = "USA"


def getRows(filename):
    return csv.DictReader(open(filename))

def getField(line, field_number):
    return line.split(DEFAULT_DELIMITER)[field_number]

def getFields(line, start_field, end_field=None):
    if end_field:
        return line.split(DEFAULT_DELIMITER)[start_field:end_field]
    else:
        return line.split(DEFAULT_DELIMITER)[start_field:]

def isAmerican(country):
    return country == USA

def getFirstName(name):
    return name.split()[0].strip()

def getFormalName(name_conversions, name):
    if name in name_conversions:
        return name_conversions[name]
    return name

def isSignificant(count):
    return count >= COUNT_THRESHOLD

def isMale(gender):
    return gender == MALE

def isRecentYear(year):
    return int(year) >= START_YEAR
