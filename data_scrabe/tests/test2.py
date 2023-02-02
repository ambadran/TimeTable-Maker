import csv

all_raw_data = []

with open("Fall2021.csv", "r", encoding='mac_roman', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, dialect=csv.excel)
    for line in csv_reader:
        all_raw_data.append(line)

days_start_row = [] # a list of the number of the row which start a new day, e.g- row 21 is the start of subjects on Monday
for n, i in enumerate(all_raw_data):
    if i[1] != '':
        days_start_row.append(n)

raw_days_data = []
for n, i in enumerate(days_start_row):
    if n != 4:
        raw_days_data.append(all_raw_data[ days_start_row[n] : days_start_row[n+1]])
    elif n == 4:
        raw_days_data.append(all_raw_data[ days_start_row[n]:])
    
# clearing the first two values in each list, this is the first two columns which contain the number and day
for n, i in enumerate(raw_days_data):
    for j, k in enumerate(i):
        raw_days_data[n][j] = k[2:]

days = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY"]
times = ["8:30 - 9:20", "9:30 - 10:20", "10:30 - 11:20", "11:30 - 12:20", "12:30 - 1:20", "1:30 - 2:20", "2:30 - 3:20", "3:30 - 4:20"]

class subject_unorganised:
    def __init__(self, name, activity, instructor, room, day, time):
        self.name = name
        self.activity = activity
        self.instructor = instructor
        self.room = room
        self.day = day
        self.time = time

ALL_CLASSES_unorganised = []
for n, i in enumerate(raw_days_data):
    for a, b in enumerate(i):
        for j, k in enumerate(times):
            if b[j*4] != '':
                ALL_CLASSES_unorganised.append(subject_unorganised(b[j*4], b[j*4+1], b[j*4+2], b[j*4+3], days[n], k))

print(len(ALL_CLASSES_unorganised))
print(ALL_CLASSES_unorganised[100].__dict__)

















