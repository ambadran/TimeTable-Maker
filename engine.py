import csv
import os
import shutil

main_timetable = []

with open("Fall2021.csv", "r", encoding='mac_roman', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, dialect=csv.excel)
    for line in csv_reader:
        main_timetable.append(line)

class subject_unorganised:
    def __init__(self, name, activity, instructor, room, day, time):
        self.name = name
        self.activity = activity
        self.instructor = instructor
        self.room = room
        self.day = day
        self.time = time
    def concatinate(self):
        self.name = f"{self.name}-{self.activity}"

days = []
for i in main_timetable:
    for n in ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY"]:
        if i[1] == n:
            days.append(int(i[0]))

for i in main_timetable:
    if i[0] != "":
        i[0] = int(i[0])

ALL_CLASSES_unorganised_unfiltered = []
for n, i in enumerate(main_timetable):
    if n > 1:
        if i[0] >= days[0] and i[0] < days[1]:
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[2], i[3], i[4], i[5], "SUNDAY", "8:30 - 9:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[6], i[7], i[8], i[9], "SUNDAY", "9:30 - 10:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[10], i[11], i[12], i[13], "SUNDAY", "10:30 - 11:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[14], i[15], i[16], i[17], "SUNDAY", "11:30 - 12:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[18], i[19], i[20], i[21], "SUNDAY", "12:30 - 1:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[22], i[23], i[24], i[25], "SUNDAY", "1:30 - 2:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[26], i[27], i[28], i[29], "SUNDAY", "2:30 - 3:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[30], i[31], i[32], i[33], "SUNDAY", "3:30 - 4:20"))
        elif i[0] >= days[1] and i[0] < days[2]:
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[2], i[3], i[4], i[5], "MONDAY", "8:30 - 9:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[6], i[7], i[8], i[9], "MONDAY", "9:30 - 10:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[10], i[11], i[12], i[13], "MONDAY", "10:30 - 11:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[14], i[15], i[16], i[17], "MONDAY", "11:30 - 12:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[18], i[19], i[20], i[21], "MONDAY", "12:30 - 1:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[22], i[23], i[24], i[25], "MONDAY", "1:30 - 2:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[26], i[27], i[28], i[29], "MONDAY", "2:30 - 3:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[30], i[31], i[32], i[33], "MONDAY", "3:30 - 4:20"))
        elif i[0] >= days[2] and i[0] < days[3]:
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[2], i[3], i[4], i[5], "TUESDAY", "8:30 - 9:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[6], i[7], i[8], i[9], "TUESDAY", "9:30 - 10:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[10], i[11], i[12], i[13], "TUESDAY", "10:30 - 11:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[14], i[15], i[16], i[17], "TUESDAY", "11:30 - 12:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[18], i[19], i[20], i[21], "TUESDAY", "12:30 - 1:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[22], i[23], i[24], i[25], "TUESDAY", "1:30 - 2:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[26], i[27], i[28], i[29], "TUESDAY", "2:30 - 3:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[30], i[31], i[32], i[33], "TUESDAY", "3:30 - 4:20"))
        elif i[0] >= days[3] and i[0] < days[4]:
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[2], i[3], i[4], i[5], "WEDNESDAY", "8:30 - 9:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[6], i[7], i[8], i[9], "WEDNESDAY", "9:30 - 10:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[10], i[11], i[12], i[13], "WEDNESDAY", "10:30 - 11:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[14], i[15], i[16], i[17], "WEDNESDAY", "11:30 - 12:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[18], i[19], i[20], i[21], "WEDNESDAY", "12:30 - 1:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[22], i[23], i[24], i[25], "WEDNESDAY", "1:30 - 2:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[26], i[27], i[28], i[29], "WEDNESDAY", "2:30 - 3:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[30], i[31], i[32], i[33], "WEDNESDAY", "3:30 - 4:20"))
        elif i[0] >= days[4]:
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[2], i[3], i[4], i[5], "THURSDAY", "8:30 - 9:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[6], i[7], i[8], i[9], "THURSDAY", "9:30 - 10:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[10], i[11], i[12], i[13], "THURSDAY", "10:30 - 11:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[14], i[15], i[16], i[17], "THURSDAY", "11:30 - 12:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[18], i[19], i[20], i[21], "THURSDAY", "12:30 - 1:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[22], i[23], i[24], i[25], "THURSDAY", "1:30 - 2:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[26], i[27], i[28], i[29], "THURSDAY", "2:30 - 3:20"))
            ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[30], i[31], i[32], i[33], "THURSDAY", "3:30 - 4:20"))

ALL_CLASSES_unorganised = []
for i in ALL_CLASSES_unorganised_unfiltered:
    if i.name != "":
        ALL_CLASSES_unorganised.append(i)

LEC = []
TUT = []
LAB = []

for i in ALL_CLASSES_unorganised:
    if i.activity[0:3] == "LEC":
        LEC.append(i)
    elif i.activity[0:3] == "TUT":
        TUT.append(i)
    elif i.activity[0:3] == "LAB":
        LAB.append(i)


class subject:
    def __init__(self, name, activity, instructor, times, room="NA"):
        self.name = name
        try:
            self.section = int(name.split('-')[1])
        except Exception:
            self.section = int(name.split('-')[1][:-1])
            self.division = name.split('-')[1][2]
        self.activity = activity
        self.instructor = instructor
        self.times = times
        self.room = room

### LEC ####################################
for i in LEC: #################################### testing
    i.concatinate()
dicta = {}
for i in LEC:
    dicta[i.name] = set()

for i in LEC:
    for n in dicta.keys():
        dicta[i.name].add(f"{i.day}@{i.time}")

ALL_CLASSES_LEC = []
for i, n in dicta.items():
    for k in LEC:
        if i == k.name:
            ALL_CLASSES_LEC.append(subject(k.name, k.activity, k.instructor, sorted(list(n)), k.room))
            break
# for i in ALL_CLASSES_LEC: # now i have list of unique lecture classes
#     print(i.name, i.times)

#########################################################

### TUT ###
for i in TUT:
    i.concatinate()
dictb = {}
for i in TUT:
    dictb[i.name] = set()

for i in TUT:
    for n in dictb.keys():
        dictb[i.name].add(f"{i.day}@{i.time}")

ALL_CLASSES_TUT = []
for i, n in dictb.items():
    for k in TUT:
        if i == k.name:
            ALL_CLASSES_TUT.append(subject(k.name, k.activity, k.instructor, sorted(list(n)), k.room))
            break
# for i in ALL_CLASSES_TUT:
#     print(i.name, i.times)

####################################################

### LAB ###
for i in LAB:
    i.concatinate()
dictc = {}
for i in LAB:
    dictc[i.name] = set()

for i in LAB:
    for n in dictc.keys():
        dictc[i.name].add(f"{i.day}@{i.time}")

ALL_CLASSES_LAB = []
for i, n in dictc.items():
    for k in LAB:
        if i == k.name:
            ALL_CLASSES_LAB.append(subject(k.name, k.activity, k.instructor, sorted(list(n)), k.room))
            break
# for i in ALL_CLASSES_LAB:
#     print(i.name, i.times)

####################################################

def generateSubTimes(subject):
    subject_timings = [[], [], []]  # a list of 3 lists each representing LEC, TUT and LAB possible timings
    for i in ALL_CLASSES_LEC:
        if i.name[:len(subject)] == subject:
            subject_timings[0].append(i)
    for i in ALL_CLASSES_TUT:
        if i.name[:len(subject)] == subject:
            subject_timings[1].append(i)
    for i in ALL_CLASSES_LAB:
        if i.name[:len(subject)] == subject:
            subject_timings[2].append(i)
    return subject_timings

# for i in generateSubTimes("ECEN202"):
#     print(i)
#     for n in i:
#         print(n.__dict__)


def generateAllSublist(name_subjects):
    '''genreate a list of lists, each list is a list of the possible subject variables
    note that lec , tut and lab are each in a different list and treated as independent subjects with
    their own variables'''
    ALL_SUBJECTS_unfiltered = []
    for i in name_subjects:
        ALL_SUBJECTS_unfiltered.extend(generateSubTimes(i))
    ALL_SUBJECTS = []
    for i in ALL_SUBJECTS_unfiltered:
        if i != []:
            ALL_SUBJECTS.append(i)
    return ALL_SUBJECTS

# for i in generateAllSublist(["ECEN204", "MATH206", "ECEN203", "ECEN202", "ENGL102", "ENTR301"]):
#     print(i)
#     for n in i:
#         print(n.__dict__)


def check_subject(subject, possible_timetable):
    """in the timetable generating algorithm, this function checks
     subjects to not overlap with other subjects already
    in the possible timetable"""
    for i in possible_timetable:
        for a in i.times:
            for b in subject.times:
                if a == b:
                    return False
    else:
        return True

def check_timetable(timetable):
    """checks if given timetable has no time overlapping subjects"""
    condition = True
    for n, i in enumerate(timetable):
        for l, k in enumerate(timetable):
            if n != l:
                for a in i.times:
                    for b in k.times:
                        if a == b:
                            condition = False
    else:
        if condition:
            return True
        else:
            return False

def testTimeTable(TimeTable, ALL_SUBJECTS, mode):
    """This function tests a timetable for 2 things:
    TEST1-checks if the timetable generated doesn't have any subjects overlaping in time
    TEST2-checks if the timetable has all the subjects with all their lecs, tuts and labs
    mode False return True or False depending on whether the timetable is True in both tests or not
    mode True returns a detailed analysis of the tests"""

    result1 = False  # for test1
    result2 = False  # for test2

    #test1
    condition = True
    for n, i in enumerate(TimeTable):
        for l, k in enumerate(TimeTable):
            if n != l:
                for a in i.times:
                    for b in k.times:
                        if a == b:
                            condition = False
    else:
        if condition:
            result1 = True


    #test2
    x = True
    subjects = []  # subjects not found
    for i in ALL_SUBJECTS:
        for n in i:
            for k in TimeTable:
                if n.name == k.name:
                    break
            if n.name == k.name:
                break
        else:
            x = False
            subjects.append(n)
    result2 = x

    if mode:
        return f"""Overlaping Test: {result1}\nContains ALl Subject Test: {result2}\n{f'Subjects not in TimeTable: {[n.name for n in subjects]}' if not result2 else ''}"""
    else:
        return True if result1 and result2 else False

def testTimeTables(TimeTables, ALL_SUBJECTS, mode):
    """Applies testTimeTable function on all the timetables in the a list,
    then returns a list of all the invalid timetables"""
    wrong_timetables = []
    condition = False
    for i in TimeTables:
        if testTimeTable(i, ALL_SUBJECTS, mode) == False:
            condition = True
            wrong_timetables.append(i)
    else:
        if condition:
            return f"Wrong Timetables: {wrong_timetables}"
        else:
            return f"All Timetables are valid."

def testDuplicateTimeTables(TimeTables, mode):
    """tests if the input list of timetables has any duplicates
    :mode True: returns how many distinct timetables there is
    :mode False: returns a list of the duplicates as numbers according to the order of the timttables list"""
    memo = []
    for n, i in enumerate(TimeTables):
        condition = True
        for d in memo:
            if n in d:
                condition = False
        else:
            if condition:
                memo.append([n])
        for a, k in enumerate(TimeTables):
            if n != a:
                if i == k:
                    for f in memo:
                        if n in f and a not in f:
                            f.append(a)
    filtered_memo = []
    for i in memo:
        if len(i) != 1:
            filtered_memo.append(i)
    if mode:
        return len(memo)
    else:
        if len(TimeTables) == len(memo):
            return "There is no duplicate timetables in this timetables."
        else:
            return f"Duplicate Timetables: {filtered_memo}"

def createCSVlists(timeTables, mode):
    """creates a csv list to make the csv file
        mode True is for one timetables
        mode False is for many timetable"""
    if mode:
        masterlist = []
        days = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY"]
        times = ["8:30 - 9:20", "9:30 - 10:20", "10:30 - 11:20", "11:30 - 12:20", "12:30 - 1:20", "1:30 - 2:20",
                 "2:30 - 3:20", "3:30 - 4:20"]
        for i in days:
            masterlist.append([i])
        for a in range(len(days)):
            for j in range(len(times)):
                condition = False
                for i in timeTables:
                        for k in i.times:
                            if k[:len(days[a])] == days[a]:
                                if k[-len(times[j]):] == times[j]:
                                    masterlist[a].append(f"{i.name} - {i.room}")
                                    condition = True
                else:
                    if condition == False:
                        masterlist[a].append("")
        return masterlist
    else:
        masterlists = []
        for w in timeTables:
            masterlist = []
            days = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY"]
            times = ["8:30 - 9:20", "9:30 - 10:20", "10:30 - 11:20", "11:30 - 12:20", "12:30 - 1:20", "1:30 - 2:20",
                     "2:30 - 3:20", "3:30 - 4:20"]
            for i in days:
                masterlist.append([i])
            for a in range(len(days)):
                for j in range(len(times)):
                    condition = False
                    for i in w:
                        for k in i.times:
                            if k[:len(days[a])] == days[a]:
                                if k[-len(times[j]):] == times[j]:
                                    masterlist[a].append(f"{i.name} - {i.room}")
                                    condition = True
                    else:
                        if condition == False:
                            masterlist[a].append("")
            masterlists.append(masterlist)
        return masterlists



def exportTimeTable(timeTableList, mode):
    """creates a csv file to display timetables
    mode True is for one timetables
    mode False is for many timetable"""
    if mode:
        with open("TimeTable.csv", mode="w") as timeTable:
            timeTable_writer = csv.writer(timeTable, delimiter=",", quotechar='"')
            timeTable_writer.writerow(['', "8:30 - 9:20", "9:30 - 10:20", "10:30 - 11:20", "11:30 - 12:20", "12:30 - 1:20", "1:30 - 2:20", "2:30 - 3:20", "3:30 - 4:20"])
            for i in range(len(timeTableList)):
                timeTable_writer.writerow(timeTableList[i])
    else:
        try:
            os.mkdir("TimeTables")
        except FileExistsError:
            shutil.rmtree("TimeTables")
            os.mkdir("TimeTables")
        os.chdir("TimeTables")
        for s in range(len(timeTableList)):
            with open(f"TimeTable{s}.csv", mode="w") as timeTable:
                timeTable_writer = csv.writer(timeTable, delimiter=",", quotechar='"')
                timeTable_writer.writerow(['', "8:30 - 9:20", "9:30 - 10:20", "10:30 - 11:20", "11:30 - 12:20", "12:30 - 1:20", "1:30 - 2:20", "2:30 - 3:20", "3:30 - 4:20"])
                for i in range(len(timeTableList[s])):
                    timeTable_writer.writerow(timeTableList[s][i])

def checkSubinMain(subject):
    '''checks if subject is found in main timetable or not'''
    for i in generateSubTimes(subject):
        if i:
            return True # subject found in Main TimeTable
    else:
        return False # subject not found in Main TimeTable

###################################################################################
if __name__ == "__main__":
#    print(checkSubinMain("ECEN305"))
    for i in generateSubTimes("HUMA002"):
         print(i)
         for n in i:
             print(n.__dict__)
    # for i in generateAllSublist(["ECEN204", "MATH206", "ECEN203", "ECEN202", "ENGL102", "ENTR301"]):
    #     print(i)
    #     for n in i:
    #         print(n.__dict__)







