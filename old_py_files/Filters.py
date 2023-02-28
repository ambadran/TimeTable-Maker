from timetable_generating_algorithm_old import *
import pickle

def Filter(TimeTables, filters, mode):
    """put the filter names wanted in a list in filters argument, filters will be applied in the order of the list
    supported Filters:
    1- "same_section" --> return all timetables that has the same section number in each subject

    mode="debug" --> return modified timetable and prints number of timetables after filtering
    mode="exec" --> reutrn modified timetables only"""

    if "same_section" in filters:
        new = []
        for i in TimeTables:
            condition = True
            for c, a in enumerate(i):
                for d, b in enumerate(i):
                    if c != d:
                        if a.name.split('-')[0] == b.name.split('-')[0]:
                            if a.section != b.section:
                                condition = False
            else:
                if condition:
                    new.append(i)

        if mode == "debug":
            print(f"Number of possible Timetables with same section in each subject: {len(new)}")
        elif mode == "exec":
            pass
        else:
            raise ValueError("Mode not supported")

    if "offline_Thurs" in filters:
        new = []
        count = 0
        for TimeTable in TimeTables:
            condition = True
            for i in TimeTable:
                for n in i.times:
                    if "THURSDAY" in n and i.room == 'online':
                        condition = False 
                        count += 1
                        break
            if condition:
                new.append(TimeTable)

        if mode == "debug":
            print(f"Number of possible Timetables with offline lec/tut/lab only in Thursdays: {len(new)}")
        elif mode == "exec":
            pass
        else:
            raise ValueError("Mode not supported")

    if "online_Tues" in filters:
        new = []
        for TimeTable in TimeTables:
            condition = True
            for i in TimeTable:
                for n in i.times:
                    if "TUESDAY" in n and i.room != 'online':
                        condition = False 
                        break
            if condition:
                new.append(TimeTable)

        if mode == "debug":
            print(f"Number of possible Timetables with online lec/tut/lab only in Tuesday: {len(new)}")
        elif mode == "exec":
            pass
        else:
            raise ValueError("Mode not supported")

    if "online_ALL" in filters:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        for z in days:
            new = []
            for TimeTable in TimeTables:
                condition = True
                for i in TimeTable:
                    for n in i.times:
                        if z in n and i.room != 'online':
                            condition = False 
                            break
                if condition:
                    new.append(TimeTable)
            if len(z) > 0: #TODO: fix this shit
                break

        if mode == "debug":
            print(f"Number of possible Timetables with online lec/tut/lab only in {z}: {len(new)}")
        elif mode == "exec":
            pass
        else:
            raise ValueError("Mode not supported")


    if "first2gab" in filters:
        new = []
        for TimeTable in TimeTables:
            condition = True
            for i in TimeTable:
                for n in i.times:
                    if "8:30 - 9:20" in n or "9:30 - 10:20" in n:
                        condition = False
                        break
            if condition:
                new.append(TimeTable)

        if mode == "debug":
            print(f"Number of possible Timetables with no first two periods: {len(new)}")
        elif mode == "exec":
            pass
        else:
            raise ValueError("Mode not supported")

    if "last1gab" in filters:
        new = []
        for TimeTable in TimeTables:
            condition = True
            for i in TimeTable:
                for n in i.times:
                    if "10:30 - 11:20" in n:
                        condition = False
                        break
            if condition:
                new.append(TimeTable)

        if mode == "debug":
            print(f"Number of possible Timetables with no last period: {len(new)}")
        elif mode == "exec":
            pass
        else:
            raise ValueError("Mode not supported")


    return new




if __name__ == "__main__":
    TimeTables = retrieveTimeTable()
    print(len(TimeTables))
    # applying filters
    mod1 = Filter(TimeTables, ["same_section"], "debug")

    for timetable in mod1:
        for sub in timetable:
            print(sub.name, sub.activity, sub.times)
        print()
        print()

    #  exporting filtered timetables into csv files
    exportTimeTable(createCSVlists(mod1, False), False)
    

    





