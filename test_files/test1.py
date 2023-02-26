import csv


with open("semister2 main.csv", encoding='mac_roman', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        print(": ".join(row))
