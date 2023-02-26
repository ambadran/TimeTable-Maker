from engine import *
import pickle
import time

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

def generateTimeTables(ALL_SUBJECTS, mode):
    """Main function is to generate all possible timetables that has 3 characteristics:
    1- no overlapping subjects time-wise
    2- all wanted subjects with all their lec, tut and labs are present in each timetable generated
    3- no duplicate timetables
    mode="debug" --> return len_sub, number of possible timetables, calctime and export TimeTables to pickle
            object, all in a tuble in this order
    mode="exec" --> exports TimeTables to pickle object and return spent_time only"""
    len_sub = len(ALL_SUBJECTS)
    TimeTables = []
    start_time = time.time()
    # if mode == "debug":
    #     print("Loading...")
    if len_sub == 1:
        current = 0
        length = 1
        for i in range(len(ALL_SUBJECTS)):
            length *= len(ALL_SUBJECTS[i])
        for a in ALL_SUBJECTS[0]:
            if check_timetable([a]):
                TimeTables.append([a])
            current += 1
            printProgressBar(current, length, prefix='Progress:',
                             suffix='Complete', length=50)
    elif len_sub == 2:
        current = 0
        length = 1
        for i in range(len(ALL_SUBJECTS)):
            length *= len(ALL_SUBJECTS[i])
        for a in ALL_SUBJECTS[0]:
            for b in ALL_SUBJECTS[1]:
                if check_timetable([a, b]):
                    TimeTables.append([a, b])
                current += 1
                printProgressBar(current, length, prefix='Progress:',
                                 suffix='Complete', length=50)
    elif len_sub == 3:
        current = 0
        length = 1
        for i in range(len(ALL_SUBJECTS)):
            length *= len(ALL_SUBJECTS[i])
        for a in ALL_SUBJECTS[0]:
            for b in ALL_SUBJECTS[1]:
                for c in ALL_SUBJECTS[2]:
                    if check_timetable([a, b, c]):
                        TimeTables.append([a, b, c])
                    current += 1
                    printProgressBar(current, length, prefix='Progress:',
                                     suffix='Complete', length=50)
    elif len_sub == 4:
        current = 0
        length = 1
        for i in range(len(ALL_SUBJECTS)):
            length *= len(ALL_SUBJECTS[i])
        for a in ALL_SUBJECTS[0]:
            for b in ALL_SUBJECTS[1]:
                for c in ALL_SUBJECTS[2]:
                    for d in ALL_SUBJECTS[3]:
                        if check_timetable([a, b, c, d]):
                            TimeTables.append([a, b, c, d])
                        current += 1
                        printProgressBar(current, length, prefix='Progress:',
                                         suffix='Complete', length=50)
    elif len_sub == 5:
        current = 0
        length = 1
        for i in range(len(ALL_SUBJECTS)):
            length *= len(ALL_SUBJECTS[i])
        for a in ALL_SUBJECTS[0]:
            for b in ALL_SUBJECTS[1]:
                for c in ALL_SUBJECTS[2]:
                    for d in ALL_SUBJECTS[3]:
                        for e in ALL_SUBJECTS[4]:
                            if check_timetable([a, b, c, d, e]):
                                TimeTables.append([a, b, c, d, e])
                            current += 1
                            printProgressBar(current, length, prefix='Progress:',
                                             suffix='Complete', length=50)
    elif len_sub == 6:
        current = 0
        length = 1
        for i in range(len(ALL_SUBJECTS)):
            length *= len(ALL_SUBJECTS[i])
        for a in ALL_SUBJECTS[0]:
            for b in ALL_SUBJECTS[1]:
                for c in ALL_SUBJECTS[2]:
                    for d in ALL_SUBJECTS[3]:
                        for e in ALL_SUBJECTS[4]:
                            for f in ALL_SUBJECTS[5]:
                                if check_timetable([a, b, c, d, e, f]):
                                    TimeTables.append([a, b, c, d, e, f])
                                current += 1
                                printProgressBar(current, length, prefix='Progress:',
                                                 suffix='Complete', length=50)
    elif len_sub == 7:
        current = 0
        length = 1
        for i in range(len(ALL_SUBJECTS)):
            length *= len(ALL_SUBJECTS[i])
        for a in ALL_SUBJECTS[0]:
            for b in ALL_SUBJECTS[1]:
                for c in ALL_SUBJECTS[2]:
                    for d in ALL_SUBJECTS[3]:
                        for e in ALL_SUBJECTS[4]:
                            for f in ALL_SUBJECTS[5]:
                                for g in ALL_SUBJECTS[6]:
                                    if check_timetable([a, b, c, d, e, f, g]):
                                        TimeTables.append([a, b, c, d, e, f, g])
                                    current += 1
                                    printProgressBar(current, length, prefix='Progress:',
                                                     suffix='Complete', length=50)
    elif len_sub == 8:
        current = 0
        length = 1
        for i in range(len(ALL_SUBJECTS)):
            length *= len(ALL_SUBJECTS[i])
        for a in ALL_SUBJECTS[0]:
            for b in ALL_SUBJECTS[1]:
                for c in ALL_SUBJECTS[2]:
                    for d in ALL_SUBJECTS[3]:
                        for e in ALL_SUBJECTS[4]:
                            for f in ALL_SUBJECTS[5]:
                                for g in ALL_SUBJECTS[6]:
                                    for h in ALL_SUBJECTS[7]:
                                        if check_timetable([a, b, c, d, e, f, g, h]):
                                            TimeTables.append([a, b, c, d, e, f, g, h])
                                        current += 1
                                        printProgressBar(current, length, prefix='Progress:',
                                                         suffix='Complete', length=50)
    elif len_sub == 9:
        current = 0
        length = 1
        for i in range(len(ALL_SUBJECTS)):
            length *= len(ALL_SUBJECTS[i])
        for a in ALL_SUBJECTS[0]:
            for b in ALL_SUBJECTS[1]:
                for c in ALL_SUBJECTS[2]:
                    for d in ALL_SUBJECTS[3]:
                        for e in ALL_SUBJECTS[4]:
                            for f in ALL_SUBJECTS[5]:
                                for g in ALL_SUBJECTS[6]:
                                    for h in ALL_SUBJECTS[7]:
                                        for i in ALL_SUBJECTS[8]:
                                            if check_timetable([a, b, c, d, e, f, g, h, i]):
                                                TimeTables.append([a, b, c, d, e, f, g, h, i])
                                            current += 1
                                            printProgressBar(current, length, prefix='Progress:',
                                                             suffix='Complete', length=50)
    elif len_sub == 10:
        current = 0
        length = 1
        for i in range(len(ALL_SUBJECTS)):
            length *= len(ALL_SUBJECTS[i])
        for a in ALL_SUBJECTS[0]:
            for b in ALL_SUBJECTS[1]:
                for c in ALL_SUBJECTS[2]:
                    for d in ALL_SUBJECTS[3]:
                        for e in ALL_SUBJECTS[4]:
                            for f in ALL_SUBJECTS[5]:
                                for g in ALL_SUBJECTS[6]:
                                    for h in ALL_SUBJECTS[7]:
                                        for i in ALL_SUBJECTS[8]:
                                            for j in ALL_SUBJECTS[9]:
                                                if check_timetable([a, b, c, d, e, f, g, h, i, j]):
                                                    TimeTables.append([a, b, c, d, e, f, g, h, i, j])
                                                current += 1
                                                printProgressBar(current, length, prefix='Progress:',
                                                                 suffix='Complete', length=50)
    elif len_sub == 11:
        current = 0
        length = 1
        for i in range(len(ALL_SUBJECTS)):
            length *= len(ALL_SUBJECTS[i])
        for a in ALL_SUBJECTS[0]:
            for b in ALL_SUBJECTS[1]:
                for c in ALL_SUBJECTS[2]:
                    for d in ALL_SUBJECTS[3]:
                        for e in ALL_SUBJECTS[4]:
                            for f in ALL_SUBJECTS[5]:
                                for g in ALL_SUBJECTS[6]:
                                    for h in ALL_SUBJECTS[7]:
                                        for i in ALL_SUBJECTS[8]:
                                            for j in ALL_SUBJECTS[9]:
                                                for k in ALL_SUBJECTS[10]:
                                                    if check_timetable([a, b, c, d, e, f, g, h, i, j, k]):
                                                        TimeTables.append([a, b, c, d, e, f, g, h, i, j, k])
                                                    current += 1
                                                    printProgressBar(current, length, prefix='Progress:',
                                                                     suffix='Complete', length=50)
    elif len_sub == 12:
        current = 0
        length = 1
        for i in range(len(ALL_SUBJECTS)):
            length *= len(ALL_SUBJECTS[i])
        for a in ALL_SUBJECTS[0]:
            for b in ALL_SUBJECTS[1]:
                for c in ALL_SUBJECTS[2]:
                    for d in ALL_SUBJECTS[3]:
                        for e in ALL_SUBJECTS[4]:
                            for f in ALL_SUBJECTS[5]:
                                for g in ALL_SUBJECTS[6]:
                                    for h in ALL_SUBJECTS[7]:
                                        for i in ALL_SUBJECTS[8]:
                                            for j in ALL_SUBJECTS[9]:
                                                for k in ALL_SUBJECTS[10]:
                                                    for l in ALL_SUBJECTS[11]:
                                                        if check_timetable([a, b, c, d, e, f, g, h, i, j, k, l]):
                                                            TimeTables.append([a, b, c, d, e, f, g, h, i, j, k, l])
                                                        current += 1
                                                        printProgressBar(current, length, prefix='Progress:',
                                                                         suffix='Complete', length=50)
    elif len_sub == 13:
        current = 0
        length = 1
        for i in range(len(ALL_SUBJECTS)):
            length *= len(ALL_SUBJECTS[i])
        for a1, a in enumerate(ALL_SUBJECTS[0]):
            for b1, b in enumerate(ALL_SUBJECTS[1]):
                for c1, c in enumerate(ALL_SUBJECTS[2]):
                    for d1, d in enumerate(ALL_SUBJECTS[3]):
                        for e1, e in enumerate(ALL_SUBJECTS[4]):
                            for f1, f in enumerate(ALL_SUBJECTS[5]):
                                for g1, g in enumerate(ALL_SUBJECTS[6]):
                                    for h1, h in enumerate(ALL_SUBJECTS[7]):
                                        for i1, i in enumerate(ALL_SUBJECTS[8]):
                                            for j1, j in enumerate(ALL_SUBJECTS[9]):
                                                for k1, k in enumerate(ALL_SUBJECTS[10]):
                                                    for l1, l in enumerate(ALL_SUBJECTS[11]):
                                                        for m1, m in enumerate(ALL_SUBJECTS[12]):
                                                            if check_timetable([a, b, c, d, e, f, g, h, i, j, k, l, m]):
                                                                TimeTables.append(
                                                                    [a, b, c, d, e, f, g, h, i, j, k, l, m])
                                                            current += 1
                                                            printProgressBar(current, length, prefix='Progress:',
                                                                             suffix='Complete', length=50)
    elif len_sub == 14:
        current = 0
        length = 1
        for i in range(len(ALL_SUBJECTS)):
            length *= len(ALL_SUBJECTS[i])
        for a1, a in enumerate(ALL_SUBJECTS[0]):
            for b1, b in enumerate(ALL_SUBJECTS[1]):
                for c1, c in enumerate(ALL_SUBJECTS[2]):
                    for d1, d in enumerate(ALL_SUBJECTS[3]):
                        for e1, e in enumerate(ALL_SUBJECTS[4]):
                            for f1, f in enumerate(ALL_SUBJECTS[5]):
                                for g1, g in enumerate(ALL_SUBJECTS[6]):
                                    for h1, h in enumerate(ALL_SUBJECTS[7]):
                                        for i1, i in enumerate(ALL_SUBJECTS[8]):
                                            for j1, j in enumerate(ALL_SUBJECTS[9]):
                                                for k1, k in enumerate(ALL_SUBJECTS[10]):
                                                    for l1, l in enumerate(ALL_SUBJECTS[11]):
                                                        for m1, m in enumerate(ALL_SUBJECTS[12]):
                                                            for n1, n in enumerate(ALL_SUBJECTS[13]):
                                                                if check_timetable(
                                                                        [a, b, c, d, e, f, g, h, i, j, k, l, m, n]):
                                                                    TimeTables.append(
                                                                        [a, b, c, d, e, f, g, h, i, j, k, l, m, n])
                                                                current += 1
                                                                printProgressBar(current, length, prefix='Progress:',
                                                                                 suffix='Complete', length=50)
    spent_time = time.time() - start_time
    if mode == "debug":
        print(f"Total number of lectures, tutorials and labs: {len_sub}")
        if spent_time < 60:
            print(f"Time Spent: {round(spent_time)} seconds")
        else:
            print(f"Time Spend: {round(spent_time / 60)}min {round(spent_time % 60)}sec")
        # Saving the Timetables variable into a pickle storage file:
        with open('output.pkl', 'wb') as f:
            pickle.dump(TimeTables, f)
        print(f"Total number of possible TimeTables: {len(TimeTables)}")
        return TimeTables
    elif mode == "exec":
        # Saving the Timetables variable into a pickle storage file:
        with open('output.pkl', 'wb') as f:
            pickle.dump(TimeTables, f)
        return spent_time
    else:
        raise ValueError("mode not supported")

def completeTest(wanted_subjects, TimeTables):
    ALL_SUBJECTS = generateAllSublist(wanted_subjects)
    print(testDuplicateTimeTables(TimeTables, False))  # testing for duplicate timetables
    print(testTimeTables(TimeTables, ALL_SUBJECTS, False))  # testing all timetables for validity

def retrieveTimeTable():
    # Getting the stored Timetables variable:
    with open('output.pkl', 'rb') as f:
        TimeTables = pickle.load(f)
    return TimeTables

if __name__ == "__main__":
    wanted_subjects = ["ECEN204", "MATH206", "ECEN203", "ECEN202", "ENTR301", "ENGL102"]
    ALL_SUBJECTS = generateAllSublist(wanted_subjects)
    TimeTables = generateTimeTables(ALL_SUBJECTS, "debug")
    # TimeTables = retrieveTimeTable()
    completeTest(wanted_subjects, TimeTables)
