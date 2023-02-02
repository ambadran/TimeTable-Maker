

# algorithm to generate all possible timetables #################################
wanted_subjects = ["ECEN204", "MATH206", "ECEN203", "ECEN202", "ENGL102", "ENTR301"]
ALL_SUBJECTS = generateAllSublist(wanted_subjects)
possibleTimeTables = []
num = 0
for a, b in enumerate(ALL_SUBJECTS):
    for c, d in enumerate(b):
        possibleTimeTables.append([])
        one = a
        two = c
        for n in ALL_SUBJECTS:
            for i in n:
                if check_subject(i, possibleTimeTables[num]):
                    possibleTimeTables[num].append(i)
                    break
        else:
            if testTimeTable(possibleTimeTables[num], ALL_SUBJECTS, False):
                possibleTimeTables.append(possibleTimeTables[num])
            ALL_SUBJECTS = generateAllSublist(wanted_subjects)
            ALL_SUBJECTS[one].remove(ALL_SUBJECTS[one][two])
        num += 1

# temporary to remove the wrong timetables
correctTimeTables = []
for i in possibleTimeTables:
    # print(testTimeTable(possibleTimeTables[0], ALL_SUBJECTS, True))
    if len(i) == 12:
        correctTimeTables.append(i)

