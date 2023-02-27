from engine import *
from abc import ABC, abstractmethod
import time
from enum import Enum
import pickle

class Modes(Enum):
    NORMAL = 1
    DEBUG = 2


def get_variables(ALL_SUBJECTS: list[list[subject]]) -> list[str]:
    '''
    :ALL_SUBJECTS: list of all possible subject objects for wanted subjects
    :return:  a list of variables to used in the CSP algorithm
    '''
    variables = []
    for sub_list in ALL_SUBJECTS:
        variables.append(f"{sub_list[0].sub_name}_{sub_list[0].activity}")

    return variables


def get_domains(variables: list[str], ALL_SUBJECTS: list[list[subject]]) -> dict[str: list[subject]]:
    '''
    :ALL_SUBJECTS: list of all possible subject objects for wanted subjects
    return domain dict for CSP algorithm
    '''
    domains = {}
    for ind in range(len(variables)):
        domains[variables[ind]] = ALL_SUBJECTS[ind]

    return domains


class Constraint(ABC):
    '''
    Blueprint for any constraint class for this CSP framework
    '''
    def __init__(self, variables: list[str]):
        self.variables = variables  # the variables that this constraint affects

    @abstractmethod
    def satisfied(self, assignment: dict[str: subject]) -> bool:
        pass


class DistinctTimesConstraint(Constraint):
    '''
    This constraint class imposes no two class with same time in one timetable
    '''
    def __init__(self, variables: list[str]):
        super().__init__(variables)  # This constraint affects all subjects, all variables in varaibles list

    def satisfied(self, assignment: dict[str: subject]) -> bool:
        '''
        :param assignment: a dictionary which states what specific subject is choosen for each wanted subject
                            key is a variables list value and value is one of the subject object in the list of
                            the corresponding domain value
        :return : bool of whether the argument assignment is a valid assignment, aka a valid timetable

        A valid timetable is one where -No overlapping subjects time-wise-
        '''
        times_list = []
        for subject in assignment.values():
                times_list.extend(subject.times)

        times_set = set(times_list)

        return len(times_list) == len(times_set)


class SameSectionConstraint(Constraint):
    '''
    This constraint class imposes one subject must have same section in Lecture, tutorial and lab classes
    '''
    def __init__(self, variables: list[str]):
        super().__init__(variables) # This constraint affects all subjects, all variables in varaibles list

    def satisfied(self, assignment: dict[str: subject]) -> bool:
        '''
        :param assignment: a dictionary which states what specific subject is choosen for each wanted subject
                            key is a variables list value and value is one of the subject object in the list of
                            the corresponding domain value
        :return: bool of whether the argument assignment is a valid assignment, aka a valid timetable

        section attribute of every subject that is of the same sub name must the same
        '''

        # creating lists of the section numbers in each subject
        sub_dict = {}
        for sub in assignment.values():
            if sub.sub_name not in sub_dict.keys():
                sub_dict[sub.sub_name] = [sub.section]
            else:
                sub_dict[sub.sub_name].append(sub.section)

        # checking the list of section numbers they must have all same values
        for section_list in sub_dict.values():
            if len(set(section_list)) != 1:
                return False

        return True




class CSP:
    '''
    Constraint Satisfactory Problem framework class
    '''

    def __init__(self, variables: list[str], domains: dict[str: list[subject]]):
        '''
        assigning variables list, domains list and creating an empty constraints dict for CSP framework
        '''
        self.variables = variables
        self.domains = domains

        self.constraints = {}
        for variable in self.variables:
            self.constraints[variable] = []

            if variable not in self.domains:
                raise LookupError("Variable not in domain dictionary")

    def add_constraint(self, constraint: Constraint):
        '''
        add the argument constraint object to every object in the constraint .variable attribute
        '''
        for variable in constraint.variables:

            if variable not in self.variables:
                raise LookupError("Constraint affecting a variable that is not in the CSP framework")

            self.constraints[variable].append(constraint)

    def consistent(self, variable: str, assignment: dict[str: subject]) -> bool:
        '''
        :param variable: the variable we want to check, (the subject code and activity value) in variables list
        :param assignment: a dictionary which states what specific subject is choosen for each wanted subject
                    key is a variables list value and value is one of the subject object in the list of
                    the corresponding domain value

        :return: whether the varaible's assigned cosntraints are all satisfied
        '''
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False

        return True

    def find_first_solution(self) -> list[subject]:
        '''
        DP Algorithm to find the first timetable it finds

        :return : list of list of subjects, list of subjects which satisfy constraints, aka list of TimeTables :)
        '''
        assignments = {}

        current_layer = 0

        last_possible_value_inds = []

        visited = set()

        while len(assignments) < len(self.variables):

            current_variable = self.variables[current_layer]
            current_domain = self.domains[current_variable]

            if current_layer == len(last_possible_value_inds):
                # never reached this level before
                last_possible_value_inds.append(0)

            elif current_layer > len(last_possible_value_inds):
                raise ValueError("WTF?!??!")

            last_possible_value_ind = last_possible_value_inds[current_layer]

            # print(current_variable, current_layer) # FOR DEBUGGING
            
            for possible_value_ind in range(last_possible_value_ind, len(current_domain)):

                assignments[current_variable] = current_domain[possible_value_ind]

                last_possible_value_inds[current_layer] = possible_value_ind
                # print(possible_value_ind, len(current_domain)) # FOR DEBUGGING

                if self.consistent(current_variable, assignments) and tuple(last_possible_value_inds) not in visited:

                    # print(last_possible_value_inds) # FOR DEBUGGING

                    current_layer += 1

                    break
                else:
                    visited.add(tuple(last_possible_value_inds))
            else:
                # no value in this layer is consistent with current combination of values in assignments dict
                # Thus, backtracking

                # print('backtracking') # FOR DEBUGGING

                if current_variable in assignments:
                    del assignments[current_variable]

                visited.add(tuple(last_possible_value_inds))  #TODO: try type casting to tuple, maybe will be faster

                last_possible_value_inds[current_layer] = 0

                current_layer -= 1

                last_possible_value_inds[current_layer] += 1

                # print(last_possible_value_inds) # FOR DEBUGGING

                if current_layer == -1:
                    possible_time_table_to_be_found = False
                    return None # No possible timetable found

        timetable = list(assignments.values())
        # for sub in timetable:
            # print(sub.name, sub.section, sub.times) # FOR DEBUGGING

        return timetable


    def find_all_solutions(self) -> list[list[subject]]:
        '''
        DP Algorithm to find every possible solution to this CSP

        :return : list of list of subjects, list of subjects which satisfy constraints, aka list of TimeTables :)

        exact same algorithm as find_first_solution but now whenever it finds a correct timetable,
        it just adds it to visited set
        '''
        pass

def generateTimeTables(ALL_SUBJECTS: list[list[subject]], mode=Modes.NORMAL) -> list[list[subject]]:
    '''
    :param ALL_SUBJECTS:
    :return: list of list of subjects, aka list of timetables
    '''

    if mode == Modes.DEBUG:
        #TODO: develop proper performance code
        pass

    # Creating CSP environment
    variables = get_variables(ALL_SUBJECTS)

    domains = get_domains(variables, ALL_SUBJECTS)
    # for i in range(len(domains)):
    #     print(domains[variables[i]][0])

    csp = CSP(variables, domains)
    csp.add_constraint(DistinctTimesConstraint(variables))
    csp.add_constraint(SameSectionConstraint(variables))

    # Getting all possible solution to CSP
    result = csp.find_first_solution()



    if mode == Modes.DEBUG:
        #TODO: develop proper performance code
        # spent_time = time.time() - start_time
        print(f"Total number of lectures, tutorials and labs: {len_sub}")
        if spent_time < 60:
            print(f"Time Spent: {round(spent_time)} seconds")
        else:
            print(f"Time Spend: {round(spent_time / 60)}min {round(spent_time % 60)}sec")
        print(f"Total number of possible TimeTables: {len(TimeTables)}")


    # # Saving result in pkl file
    # with open('output.pkl', 'wb') as f:
    #     pickle.dump(all_results, f)

    # return all_results
    return result



if __name__ == "__main__":

    # wanted_subjects = ["ECEN204", "MATH206", "ECEN203", "ECEN202", "ENTR301", "ENGL102"]

    # wanted_subs = ['CSCI205', 'CSCI112', 'HUMA102', 'MATH112']

    wanted_subs = ['ECEN311', 'ECEN313', 'HUMA002', 'ENGL102', 'ENTR301', 'MATH206', 'NSCI102', 'CHEM001']

    ALL_SUBJECTS = generateAllSublist(wanted_subs)

    result = generateTimeTables(ALL_SUBJECTS)

    for sub in result:
        print(sub.name, sub.section, sub.times) # FOR DEBUGGING
    completeTest(wanted_subs, [result])


    # TimeTables = generateTimeTables(ALL_SUBJECTS, "debug")
    # TimeTables = retrieveTimeTable()
    # completeTest(wanted_subjects, TimeTables)
