# main_timetable = []

# with open("Main_Timetable.csv", "r", encoding='mac_roman', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file, dialect=csv.excel)
#     for line in csv_reader:
#         main_timetable.append(line)

# class subject_unorganised:
#     def __init__(self, name, activity, instructor, room, day, time):
#         self.name = name
#         self.activity = activity
#         self.instructor = instructor
#         self.room = room
#         self.day = day
#         self.time = time
#     def concatinate(self):
#         self.name = f"{self.name}-{self.activity}"

# days = []
# for i in main_timetable:
#     for n in ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY"]:
#         if i[1] == n:
#             days.append(int(i[0]))

# for i in main_timetable:
#     if i[0] != "":
#         i[0] = int(i[0])

# ALL_CLASSES_unorganised_unfiltered = []
# for n, i in enumerate(main_timetable):
#     if n > 1:
#         if i[0] >= days[0] and i[0] < days[1]:
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[2], i[3], i[4], i[5], "SUNDAY", "8:30 - 9:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[6], i[7], i[8], i[9], "SUNDAY", "9:30 - 10:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[10], i[11], i[12], i[13], "SUNDAY", "10:30 - 11:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[14], i[15], i[16], i[17], "SUNDAY", "11:30 - 12:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[18], i[19], i[20], i[21], "SUNDAY", "12:30 - 1:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[22], i[23], i[24], i[25], "SUNDAY", "1:30 - 2:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[26], i[27], i[28], i[29], "SUNDAY", "2:30 - 3:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[30], i[31], i[32], i[33], "SUNDAY", "3:30 - 4:20"))
#         elif i[0] >= days[1] and i[0] < days[2]:
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[2], i[3], i[4], i[5], "MONDAY", "8:30 - 9:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[6], i[7], i[8], i[9], "MONDAY", "9:30 - 10:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[10], i[11], i[12], i[13], "MONDAY", "10:30 - 11:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[14], i[15], i[16], i[17], "MONDAY", "11:30 - 12:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[18], i[19], i[20], i[21], "MONDAY", "12:30 - 1:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[22], i[23], i[24], i[25], "MONDAY", "1:30 - 2:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[26], i[27], i[28], i[29], "MONDAY", "2:30 - 3:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[30], i[31], i[32], i[33], "MONDAY", "3:30 - 4:20"))
#         elif i[0] >= days[2] and i[0] < days[3]:
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[2], i[3], i[4], i[5], "TUESDAY", "8:30 - 9:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[6], i[7], i[8], i[9], "TUESDAY", "9:30 - 10:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[10], i[11], i[12], i[13], "TUESDAY", "10:30 - 11:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[14], i[15], i[16], i[17], "TUESDAY", "11:30 - 12:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[18], i[19], i[20], i[21], "TUESDAY", "12:30 - 1:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[22], i[23], i[24], i[25], "TUESDAY", "1:30 - 2:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[26], i[27], i[28], i[29], "TUESDAY", "2:30 - 3:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[30], i[31], i[32], i[33], "TUESDAY", "3:30 - 4:20"))
#         elif i[0] >= days[3] and i[0] < days[4]:
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[2], i[3], i[4], i[5], "WEDNESDAY", "8:30 - 9:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[6], i[7], i[8], i[9], "WEDNESDAY", "9:30 - 10:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[10], i[11], i[12], i[13], "WEDNESDAY", "10:30 - 11:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[14], i[15], i[16], i[17], "WEDNESDAY", "11:30 - 12:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[18], i[19], i[20], i[21], "WEDNESDAY", "12:30 - 1:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[22], i[23], i[24], i[25], "WEDNESDAY", "1:30 - 2:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[26], i[27], i[28], i[29], "WEDNESDAY", "2:30 - 3:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[30], i[31], i[32], i[33], "WEDNESDAY", "3:30 - 4:20"))
#         elif i[0] >= days[4]:
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[2], i[3], i[4], i[5], "THURSDAY", "8:30 - 9:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[6], i[7], i[8], i[9], "THURSDAY", "9:30 - 10:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[10], i[11], i[12], i[13], "THURSDAY", "10:30 - 11:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[14], i[15], i[16], i[17], "THURSDAY", "11:30 - 12:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[18], i[19], i[20], i[21], "THURSDAY", "12:30 - 1:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[22], i[23], i[24], i[25], "THURSDAY", "1:30 - 2:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[26], i[27], i[28], i[29], "THURSDAY", "2:30 - 3:20"))
#             ALL_CLASSES_unorganised_unfiltered.append(subject_unorganised(i[30], i[31], i[32], i[33], "THURSDAY", "3:30 - 4:20"))

# ALL_CLASSES_unorganised = []
# for i in ALL_CLASSES_unorganised_unfiltered:
#     if i.name != "":
#         ALL_CLASSES_unorganised.append(i)

# print(len(ALL_CLASSES_unorganised))
# print(ALL_CLASSES_unorganised[100].__dict__)
# # print(ALL_CLASSES_unorganised[49].__dict__)


