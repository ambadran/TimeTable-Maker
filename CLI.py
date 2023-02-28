from engine import *
from timetable_generating_algorithm import *

def makeTimeTables(wanted_subjects, *constraints):
    for i in wanted_subjects:
        if not checkSubinMain(i):
            raise LookupError(f"{i} not found in Main TimeTable")
    return generateTimeTables(generateAllSublist(wanted_subjects), *constraints)


print("""

#######################################################################################

Welcome to the TimeTable making program,

Use start_tutorial(\x1B[3mmode\x1B[0m) function for help. There are two modes:

 - for interactive tutorial (step by step guide), pass 'interactive' as mode argument
 - for non-interactive tutorial (only text), pass 'text' as mode argument
#######################################################################################


 """)



def start_tutorial(mode):
    if mode == "interactive":
        print("\nStep 1: create a list of names of the subjects you want to include in your timetable.\nE.G:\n\twanted_subs = [\"ECEN204\", \"MATH206\", \"ECEN203\", \"ECEN202\", \"ENTR301\", \"ENGL102\"]")
        k = input()
        exec(k)
        print("""Step 2: create a variable and assign it to makeTimeTables() function and pass as much arguments as you want, 
as well all the filters you want as arguments. The filters are 'Constraint' inheriting objects.
The most famous one is 'SameSectionConstraint' which is a constraint class that imposes same section number in all lec, tut, lab
E.G:
    TimeTables = makeTimeTables(wanted_subs, Mode.Debug, SameSectionConstraint)
""")
        k = input()
        exec(k)
        print("\nStep 3: call exportCSV() function and pass the previously created TimeTables variable as argument to export the generated timetables into csv files in a created TimeTable file created in the same working directory\nE.G:\n\texportCSV(TimeTables)")
        k = input()
        eval(k)
        print("\nStep 4 (optional): To check timetables for validity (no overlapping subjects in each timetable and ensure every\n timetable has all wanted subjects) and duplicity (if there is any duplicate timetables in the whole list), use:\ncompleteTest(wanted_subjects, TimeTables)\nE.G:\n\tcompleteTest(wanted_subs, TimeTables)")
        k = input()
        eval(k)
        print("\nCongrats! you now have you own custom timetables")
    elif mode == "text":
        print("""\n\nStep 1: create a list of names of the subjects you want to include in your timetable.
E.G:
    wanted_subs = [\"ECEN204\", \"MATH206\", \"ECEN203\", \"ECEN202\", \"ENTR301\", \"ENGL102\"]

Step 2: create a variable and assign it to makeTimeTables() function and pass the list you just created as argument, 
as well all the filters you want as arguments. The filters are 'Constraint' inheriting objects.
The most famous one is 'SameSectionConstraint' which is a constraint class that imposes same section number in all lec, tut, lab
E.G:
    TimeTables = makeTimeTables(wanted_subs, Mode.Debug, SameSectionConstraint)

    
Step 3: call exportCSV() function and pass the previously created TimeTables variable as argument to export the 
generated timetables into csv files in a created TimeTable file created in the same working directory
E.G:
    exportCSV(TimeTables)
    
Step 4 (optional): To check timetables for validity (no overlapping subjects in each timetable and ensure every\n 
timetable has all wanted subjects) and duplicity (if there is any duplicate timetables in the whole list), use:\n
completeTest(wanted_subjects, TimeTable)\n
E.G:\n\t
    completeTest(wanted_subs, TimeTables)""")
    else:
        print("\nmode not supported")
