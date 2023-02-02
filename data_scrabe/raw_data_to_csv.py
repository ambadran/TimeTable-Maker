import re
import csv
import pickle


class Class:
    '''
    class to extract data from one single block
    '''
    def __init__(self, course_code, activity, time, day, room, instructor):
        self.course_code = course_code
        self.activity = activity
        self.time = time
        self.day = day
        self.room = room
        self.instructor = instructor

    @classmethod
    def from_string(cls, text):

        # course code, eg-ECEN314
        subject_name = text[0:7]
        section_place = text.find("Section: ") + 9
        if not section_place:
            raise ValueError("Didn't find 'Section: ' in the raw data block")
        section = text[section_place:section_place+3].strip() #TODO: test subject_code is sth like ECEN312
        course_code = f"{subject_name}-{section}"

        # activity - finding whether its a lecture or tutorial or lab
        subtype_place = text.find("Subtype: ") + 9
        if not subtype_place:
            raise ValueError("Didn't find 'Subtype: ' in the raw data block")
        if text[subtype_place : subtype_place+7] == "Lecture":
            activity = "LEC"
        elif text[subtype_place : subtype_place+8] == "Tutorial":
            activity = "TUT"
        elif text[subtype_place : subtype_place+3] == "Lab":
            activity = "LAB"
        else:
            # raise ValueError(f"text after 'Subtype: ' in the raw data is not Lecture or Tutorial or Lab. It says: {text[subtype_place : subtype_place+9]}")
            raise ValueError(f"text after 'Subtype: ' in the raw data is not Lecture or Tutorial or Lab. It says: {text}")

        # time
        pattern1 = re.compile(r'\n\d?\d:\d\d [APap][Mm] - ')
        matches1 = pattern1.search(text)
        pattern2 = re.compile(r' - \d?\d:\d\d [APap][Mm]\n')
        matches2 = pattern2.search(text)
        
        if matches1:
            raw_time1 = matches1.__getitem__(0).strip()[:-6] + '0'
            raw_time2 = matches2.__getitem__(0).strip()[2:-4] + '0'
            time = raw_time1 + " - " + raw_time2

        else:  # testing for stupid english subjects
            if 'This class has multiple meeting times' in text:
                raise ValueError("English subject with multiple timings found")
            else:
                raise ValueError("No Proper time format found")

        # day
        pattern = re.compile(r'\n[A-Z][a-z]*day\n')
        match = pattern.search(text)
        if match:
            day = match.__getitem__(0).strip()
        else:
            raise ValueError("No day found")

        # Room
        pattern = re.compile(r'\nNile University.*\n')
        match = pattern.search(text)
        if match:
            match = match.__getitem__(0).strip()
            match = match.split(' ')
            room = match[-1]
        else:
            raise ValueError("No room found in the right format")

        #instructor
        pattern = re.compile(r'\n\w\n.*\n')
        match = pattern.search(text)
        if match:
            instructor = match.__getitem__(0)[3:].strip()
        else:
            raise ValueError("No \\n\\w\\n name \\n format found")

        return cls(course_code, activity, time, day, room, instructor)

    def __str__(self):
        '''
        for printing the object
        '''

        return str(self.__dict__)

# reading pickle file
with open('pickle_files/output2.pkl', 'rb') as f:
    # contain the string of each subject searched for (as in website) in one string value in the list
    raw_data_list: list[str] = pickle.load(f)

# converting list of course string to one big string
raw_data = "\n".join(raw_data_list)

# putting each block as one value in a big list
pattern = re.compile(r'\nNew search\n\d\d? Results\n')
match = pattern.search(raw_data)

start_from = match.end() + 1

blocks = raw_data.split('\nAdd\n\n')
blocks[0] = blocks[0][start_from:]

# converting raw string data to Class object
parsed_classes = []
for i in blocks:
    parsed_classes.append(Class.from_string(i))




# fixing the time attribute when it is two hours or more,
# Must make it more than one class object
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
times = ["8:30 - 9:20", "9:30 - 10:20", "10:30 - 11:20", "11:30 - 12:20", "12:30 - 1:20", "1:30 - 2:20", "2:30 - 3:20", "3:30 - 4:20", '4:30 - 5:20', '5:30 - 6:20']
twelve_hour_system = [i for i in range(0, 13)]
twelve_hour_system.extend(twelve_hour_system[1:])

num_wrong = 0
parsed_classes_correct_time = []
for i in parsed_classes:
    for k in times:
        if i.time == k:
            parsed_classes_correct_time.append(i)
            break
    else: # finding classes of more than one hour

        num_wrong += 1

        # finding how much hours is the class 
        pattern = re.compile(r'\d?\d:')
        matches = pattern.finditer(i.time)

        first_num = int(next(matches).__getitem__(0)[:-1])
        second_num = int(next(matches).__getitem__(0)[:-1])
        num_hours = second_num - first_num
        #dealing with 12-hour system problem
        if num_hours == 0:
            raise ValueError("WTF?!?")
        elif num_hours == 1:
            raise ValueError("should only have num_hours > 1")
        elif num_hours >= 6:
            raise ValueError("class is 6 hours or more ?!??!?")
        elif num_hours < 0:
            new_second_num = second_num + 12
            num_hours = new_second_num - first_num

        
        formatt = lambda first_num: f"{twelve_hour_system[first_num]}:30 - {twelve_hour_system[first_num+1]}:20"

        for _ in range(num_hours):
            parsed_classes_correct_time.append(Class(i.course_code, i.activity, formatt(first_num), i.day, i.room, i.instructor))
            first_num += 1



# converting .time to column number and .day to row number
for n, i in enumerate(parsed_classes_correct_time):
    parsed_classes_correct_time[n].day = days.index(i.day)
    parsed_classes_correct_time[n].time = times.index(i.time)
      
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
with open('CSVs/Main_Timetable.csv', mode='w') as timetable:
    writer = csv.writer(timetable, delimiter=',')
    for i in csv_list:
        writer.writerow(i)












