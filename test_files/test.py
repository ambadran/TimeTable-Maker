# class subject:
#     def __init__(self, name, activity, instructor, room, times):
#         self.name = name
#         self.activity = activity
#         self.instructor = instructor
#         self.room = room
#         self.times = times
#
# dicta = {}
# for i in ALL_CLASSES_unorganised:
#     dicta[i.name] = set()
#
# ALL_CLASSES = []
#
# for i in ALL_CLASSES_unorganised:
#     for n in ALL_CLASSES_unorganised:
#         if i.name == n.name:
#             if i.activity == n.activity:
#                 if i.instructor == n.instructor:
#                     dicta[i.name].add(f"{i.day}@{i.time}")
# print(dicta["MATH103-2"])

# for i in ALL_CLASSES_unorganised:
#     for n in dicta.keys():
#         if i.name == n:
#             ALL_CLASSES.append(subject(i.name, i.activity, i.instructor, i.room, dicta[n]))
#         else:
#             ALL_CLASSES.append(subject(i.name, i.activity, i.instructor, i.room, f"{i.day}@{i.time}"))
#
# for i in ALL_CLASSES:
#     print(i.name)

# number of classes per day
num_classes_day = [0, 0, 0, 0, 0]
for i in ALL_CLASSES_unorganised:
    if i.day == "SUNDAY":
        num_classes_day[0] += 1
    elif i.day == "MONDAY":
        num_classes_day[1] += 1
    elif i.day == "TUESDAY":
        num_classes_day[2] += 1
    elif i.day == "WEDNESDAY":
        num_classes_day[3] += 1
    elif i.day == "THURSDAY":
        num_classes_day[4] += 1
# total number of classes the university gives in the week
total_classes = sum(num_classes_day)


for i in LEC:
    for n in LEC:
        if i.name == n.name and i.instructor != n.instructor:
            print(i.name) # returns nothing
            ####################### THEREFORE THERE IS NO ONE CLASS TEACHED BY MORE THAN ONE PROFESSOR


num = 0
for k, i in enumerate(LEC):
    for l, n in enumerate(LEC):
        if k != l:
            if i.name == n.name and i.instructor == n.instructor and i.room == n.room and i.day == n.day and i.time == n.time:
                num +=1
                print(i.name, i.day, i.time)
print(num) ## here i proved that on thursday 9:30 to 10:20 there are duplicate subjects written by mistake in the main timetable

# ALL_SUBJECTS_times = []
# for k, i in enumerate(ALL_SUBJECTS):
#     ALL_SUBJECTS_times.append([])
#     for l, n in enumerate(i):
#         ALL_SUBJECTS_times[k].append(n.times)
        # print(n.times, ALL_SUBJECTS_times[k][l])


# possibleTimeTables = []
# for i in ALL_SUBJECTS[0]:
#     possibleTimeTables.append([i])
# for i in possibleTimeTables:
#     for n in i:
#         for k in ALL_SUBJECTS[1]:
#             if n.times != k.times:
#                 i.append(k)
#                 #create new list for the new possibility
# print(possibleTimeTables)

# results = []
# for e, i in enumerate(ALL_SUBJECTS):
#     for a, n in enumerate(i):
#         results.append([])
#         results[a].append(n)
#         for b, k in enumerate(ALL_SUBJECTS):
#             if e != b:
#                 for l in k:
#                     for c in results[a]:
#                         if c.times != l.times:
#                             results[a].append(l)
#     break

# possibleTimeTables = []
# for a, i in enumerate(ALL_SUBJECTS):
#     for n in i:
#         possibleTimeTables.append([n])
#         for b, k in enumerate(ALL_SUBJECTS):
#             if a != b:
#                 for l in k:
#                     if n.times != l.times:
#                         possibleTimeTables[0].append(l)
#                         possibleTimeTables.append([n])
#
# for i in possibleTimeTables:
#     for n in i:
#         print(n.__dict__)

