from engine import *
import pickle
import time
from itertools import permutations, combinations

wanted_subjects = ["ECEN204", "MATH206", "ECEN203", "ECEN202", "ENTR301", "ENGL102"]
ALL_SUBJECTS = generateAllSublist(wanted_subjects)
LecTutLab_num = len(ALL_SUBJECTS)
print(f"Total number of lectures, tutorials and labs: {LecTutLab_num}")
start_time = time.time()

###
TimeTables = []
def loop_rec(y, num):
    if num > 1:
        loop_rec(y, num-1)
        for i in ALL_SUBJECTS[y]:
            if check_timetable([a, b, c, d, e, f, g, h, i, j, k, l, m]):
                TimeTables.append([a, b, c, d, e, f, g, h, i, j, k, l, m])
    else:
        for i in ALL_SUBJECTS[y]:
            if check_timetable([a, b, c, d, e, f, g, h, i, j, k, l, m]):
                TimeTables.append([a, b, c, d, e, f, g, h, i, j, k, l, m])
###

# Calculating time
spent_time = time.time() - start_time
if spent_time < 60:
    print(f"Time Spent: {round(spent_time)} seconds")
else:
    print(f"Time Spend: {round(spent_time/60)}min {round(spent_time % 60)}sec")

# Saving the Timetables variable into a pickle storage file:
with open('output.pkl', 'wb') as f:
    pickle.dump(TimeTables, f)

print(f"Total number of possible TimeTables: {len(TimeTables)}")