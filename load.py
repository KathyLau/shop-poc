import csv
file = "data/black-owned-restaurants-nyc.csv"
with open(file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Address'])
