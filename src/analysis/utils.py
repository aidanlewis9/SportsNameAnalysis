import csv

def sort(d, reverse=True):
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=reverse)}

def head(d, n=1000, reverse=False):
    for k, v in list(sort(d, not reverse).items())[:n]:
        print(k.title(), v)

def show(relative_pcts, counts, n=1000, reverse=False):
    for k, v in list(sort(relative_pcts, not reverse).items())[:n]:
        print(k.title(), v, counts[k])

def writeGoodNamesToCsv(filename, relative_pcts, counts):
    with open('data/output/{}/good_names.csv'.format(filename), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Pct', 'Count'])

        for name, pct in sort(relative_pcts).items():
            writer.writerow([name.title(), pct, counts[name]])

def writeBadNamesToCsv(filename, name_pcts):
    with open('data/output/{}/bad_names.csv'.format(filename), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Pct'])

        for name, pct in sort(name_pcts).items():
            writer.writerow([name.title(), pct])
