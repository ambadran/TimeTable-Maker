

# converting .time to column number and .day to row number
for n, i in enumerate(parsed_classes_correct_time):
    parsed_classes_correct_time[n].day = days.index(i.day)
    parsed_classes_correct_time[n].time = days.index(i.time)
      
# creating the big table            
big_table = []
for n in range(len(days)):
    big_table.append([])
    for _ in range(len(times)):
        big_table[n].append([])
for i in parsed_classes_correct_time:
    big_table[i.day][i.time].append(i)
big_table[0][0].append("")

#finding the max number of subjects in one slot each day
max_ = [0 for _ in range(len(big_table))]
for d, i in enumerate(big_table):
    for n in i:
        if len(n) > max_[d]:
            max_[d] = len(n)

# filling empty slots with empty strings so that we can make the final list
for n, i in enumerate(big_table):
    for d, k in enumerate(i):
        while len(k) < max_[n]:
            big_table[n][d].append("")

# finding the row number of each day
day_row_num = []
for i in range(len(big_table)):
    if i != 0:
        day_row_num.append(len(big_table[i][0]) + day_row_num[i-1])
    else:
        day_row_num.append(len(big_table[i][0]))
day_row_num.pop()
day_row_num.insert(0, 0)

################# creating the csv list
# converting the big_table list matrix to csv list format
csv_listt = []
num = 0
for n, i in enumerate(big_table):
    for k in range(len(i[0])):
        csv_listt.append([])
        for a, b in enumerate(i):
            csv_listt[num].append(b[k])
        num += 1

csv_list = []
for k, i in enumerate(csv_listt):
    csv_list.append([])
    for a, b in enumerate(i):
        if b == '':
            csv_list[k].append('')
            csv_list[k].append('')
            csv_list[k].append('')
            csv_list[k].append('')
        elif type(b) == Class:
            csv_list[k].append(b.course_code)
            csv_list[k].append(b.activity)
            csv_list[k].append(b.instructor)
            csv_list[k].append(b.room)
               
# for n, i in enumerate(day_row_num):
#     csv_list[i].insert(0, days[n])
num = 0
for n, i in enumerate(csv_list):
    if n in day_row_num:
        csv_list[n].insert(0, days[num])
        num += 1
    else:
        csv_list[n].insert(0, '')
               

# creating the first row
current_num = 0
first_row = ["8:30 - 9:20", "9:30 - 10:20", "10:30 - 11:20", "11:30 - 12:20", "12:30 - 1:20", "1:30 - 2:20", "2:30 - 3:20", "3:30 - 4:20"]
for i in range(len(first_row)):
    for n in range(3):
        first_row.insert(current_num + 1, '')
        current_num += 1
    current_num += 1
first_row.insert(0, '')

# creating the second row
part = ["Course Code", "Activity", "Instructor", "Room"]
second_row = ['']
for _ in range(len(times)):
    second_row.extend(part)

# inserting the first and second row the csv file
csv_list.insert(0, second_row)
csv_list.insert(0, first_row)

# inserting the numbers column
col_num = 0
for n, i in enumerate(csv_list):
    csv_list[n].insert(0, col_num)
    col_num += 1

# creating the csv file
with open('Main_Timetable.csv', mode='w') as timetable:
    writer = csv.writer(timetable, delimiter=',')
    for i in csv_list:
        writer.writerow(i)












