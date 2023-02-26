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
        :return : bool of whether the argument assignment is a valid assignment, aka a valid timetables

        A valid timetable is one where -No overlapping subjects time-wise-
        '''
        times_list = []
        for subject in assignment.values():
            for time in subject.times:
                times_list.append(time)
        times_set = set(times_list)

        return len(times_list) == len(times_set)



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

    
    def find_all_solutions(self) -> list[list[subject]]:
        '''
        DP Algorithm to find every possible solution to this CSP

        :return : list of list of subjects, list of subjects which satisfy constraints, aka list of TimeTables :)
        '''
        results = []

        possible_time_table_to_be_found = True

        last_possible_value_inds = [0 for i in range(len(self.variables))]
        
        while possible_time_table_to_be_found:

            assignments = {}

            current_layer = 0


            while len(assignments) < len(self.variables):

                current_variable = self.variables[current_layer]
                current_domain = self.domains[current_variable]
                last_possible_value_ind = last_possible_value_inds[current_layer]
                
                for possible_value_ind in range(last_possible_value_ind, len(current_domain)):

                    assignments[current_variable] = current_domain[last_possible_value_ind+possible_value_ind]

                    if self.consistent(current_variable, assignments):

                        last_possible_value_inds[current_layer] = possible_value_ind

                        current_layer += 1

                        break
                else:
                    # no value in this layer is consistent with current combination of values in assignments dict
                    # Thus, backtracking
                    last_possible_value_inds[current_layer] += 1
                    if last_possible_value_inds[current_layer] == len(current_domain):
                        last_possible_value_inds[current_layer] = 0

                    current_layer -= 1

                    if current_layer == -1:
                        possible_time_table_to_be_found = False
                        break  # No possible timetable found

            for ind, val in enumerate(last_possible_value_inds):
                if val == len(current_domain):
                    last_possible_value_inds[ind] = 0
                else:
                    last_possible_value_inds[ind] += 1

            results.append(list(assignments.values()))
            print([(sub.name, sub.times) for sub in results[-1]])
            print()

        return results



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

    csp = CSP(variables, domains)
    csp.add_constraint(DistinctTimesConstraint(variables))

    # Getting all possible solution to CSP
    all_results = csp.find_all_solutions()

    if mode == Modes.DEBUG:
        #TODO: develop proper performance code
        # spent_time = time.time() - start_time
        print(f"Total number of lectures, tutorials and labs: {len_sub}")
        if spent_time < 60:
            print(f"Time Spent: {round(spent_time)} seconds")
        else:
            print(f"Time Spend: {round(spent_time / 60)}min {round(spent_time % 60)}sec")
        print(f"Total number of possible TimeTables: {len(TimeTables)}")


    # Saving result in pkl file
    with open('output.pkl', 'wb') as f:
        pickle.dump(all_results, f)

    return all_results



if __name__ == "__main__":

    # wanted_subjects = ["ECEN204", "MATH206", "ECEN203", "ECEN202", "ENTR301", "ENGL102"]

    wanted_subs = ['CSCI205', 'CSCI112', 'HUMA102', 'MATH112']

    ALL_SUBJECTS = generateAllSublist(wanted_subs)

    timetables = generateTimeTables(ALL_SUBJECTS)

    # TimeTables = generateTimeTables(ALL_SUBJECTS, "debug")
    # TimeTables = retrieveTimeTable()
    # completeTest(wanted_subjects, TimeTables)
