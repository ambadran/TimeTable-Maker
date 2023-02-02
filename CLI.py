from engine import *
from timetable_generating_algorithm import *
from Filters import *

def makeTimeTables(wanted_subjects):
    for i in wanted_subjects:
        if not checkSubinMain(i):
            raise LookupError(f"{i} not found in Main TimeTable")
    return generateTimeTables(generateAllSublist(wanted_subjects), "debug")

def exportCSV(TimeTable):
    exportTimeTable(createCSVlists(TimeTable, False), False)

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
        print("\nStep 2: create a variable and assign it to makeTimeTables() function and pass the list you just created as argument\nE.G:\n\tTimeTables = makeTimeTables(wanted_subs)")
        k = input()
        exec(k)
        print("\nStep 3: create a new variable and assign it to Filter() function to apply filters\nFirst argument is the previously created timetable, second argument is a list of the names of the filters wanted e.g- ['same_section', 'only_online', ....], third argument is the mode which is either 'debug' or 'exec' use 'debug' to get more info in cmd\nE.G:\n\t modified_TimeTable = Filter(TimeTables, ['same_section'], 'debug')")
        k = input()
        exec(k)
        print("\nStep 4: call exportCSV() function and pass the previously created TimeTables variable as argument to export the generated timetables into csv files in a created TimeTable file created in the same working directory\nE.G:\n\texportCSV(modified_TimeTable)")
        k = input()
        eval(k)
        print("\nStep 5 (optional): To check timetables for validity (no overlapping subjects in each timetable and ensure every\n timetable has all wanted subjects) and duplicity (if there is any duplicate timetables in the whole list), use:\ncompleteTest(wanted_subjects, TimeTable)\nE.G:\n\tcompleteTest(wanted_subs, modified_TimeTables)")
        k = input()
        eval(k)
        print("\nCongrats! you now have you own custom timetable")
    elif mode == "text":
        print("""\n\nStep 1: create a list of names of the subjects you want to include in your timetable.
E.G:
    wanted_subs = [\"ECEN204\", \"MATH206\", \"ECEN203\", \"ECEN202\", \"ENTR301\", \"ENGL102\"]

Step 2: create a variable and assign it to makeTimeTables() function and pass the list you just created as argument
E.G:
    TimeTables = makeTimeTables(wanted_subs)

Step 3: create a new variable and assign it to Filter() function to apply filters
First argument is the previously created timetable, second argument is a list of the names of the filters wanted
e.g- ['same_section', 'only_online', ....], third argument is the mode which is either 'debug' 
or 'exec' use 'debug' to get more info in cmd
E.G:
    modified_TimeTable = Filter(TimeTables, ['same_section'], 'debug')
    
Step 4: call exportCSV() function and pass the previously created TimeTables variable as argument to export the 
generated timetables into csv files in a created TimeTable file created in the same working directory
E.G:
    exportCSV(modified_TimeTable)
    
Step 5 (optional): To check timetables for validity (no overlapping subjects in each timetable and ensure every\n 
timetable has all wanted subjects) and duplicity (if there is any duplicate timetables in the whole list), use:\n
completeTest(wanted_subjects, TimeTable)\n
E.G:\n\t
    completeTest(wanted_subs, modified_TimeTables)""")
    else:
        print("\nmode not supported")
