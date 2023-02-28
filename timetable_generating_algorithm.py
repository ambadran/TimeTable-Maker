from engine import *
from abc import ABC, abstractmethod
import time
from enum import Enum
import pickle

pickle_file_path = 'pickle_files/time_table_generating_algorithm_output.pkl'

class Mode(Enum):
    Normal = 0
    Debug = 1

def get_variables(ALL_SUBJECTS: list[list[subject]]) -> list[str]:
    '''
    :ALL_SUBJECTS: list of all possible subject objects for wanted subjects
    :return:  a list of variables to used in the CSP algorithm
    '''
    variables = []
    for sub_list in ALL_SUBJECTS:
        variables.append(f"{sub_list[0].sub_name}_{sub_list[0].activity}")

    return variables


def get_domains(variables: [str], ALL_SUBJECTS: list[list[subject]]) -> dict[str: tuple[subject]]:
    '''
    :ALL_SUBJECTS: list of all possible subject objects for wanted subjects
    return domain dict for CSP algorithm
    '''
    domains = {}
    for ind in range(len(variables)):
        domains[variables[ind]] = tuple(ALL_SUBJECTS[ind])

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

    def find_solution_with_prints(self) -> list[subject]:
        '''
        NB: contains print statements everywhere for debugging

        DP Backtracking Algorithm to get the first Constraint-Satisfying TimeTable 

        :return: A list of subjects, A Valid TimeTable :)
        '''
        assignments: dict[str: subject] = {}  # the dictionary which maps each variable to correct value, sub_name to subject
        current_layer = 0  # the layer we are working on currently
        current_sequence = []  # It's a Stack! The path we moved through to get to current layer
        current_domain_start_ind = 0
        visited = set()  # set of tuple of correct sequence of domain indexes for each variable(sub_name+activity)
                         # will contain sequences that we know will get us to a dead-end 
                         # or that will get us to a timetable we already know

        while len(assignments) < len(self.variables):  # aka assignment dict doesn't still have all values assigned in it 

           current_variable = self.variables[current_layer]
           current_domain_values = self.domains[self.variables[current_layer]]

           print()
           print(current_variable, current_layer)

           for possible_value_ind, possible_value in enumerate(current_domain_values[current_domain_start_ind:]):

               assignments[current_variable] = possible_value

               current_sequence.append(current_domain_start_ind + possible_value_ind)

               if self.consistent(current_variable, assignments) and tuple(current_sequence) not in visited:
                   # Found a potential new path
                   print(f"Adding: {current_domain_start_ind + possible_value_ind} out of {len(current_domain_values)}")
                   print(current_sequence)
                   current_layer += 1
                   current_domain_start_ind = 0
                   break

               else:
                   # path tried doesn't satisfy constraints or already visited
                   current_sequence.pop()  
                   print(f"Skipping: {possible_value_ind} out of {len(current_domain_values)}")

           else:
                # Reached a dead-end!
                # Current Sequence have exhausted current layer's domain values

                # If no value is right in the first layer, then no possible combination will work!
                if current_layer == 0:
                    print('No Solution')
                    return None
                elif current_layer < 0:
                    raise ValueError("WTF?!??! HOW DID YOU REACH HERE?!??!")

                ### Backtracking ###
                # Go back one layer
                current_layer -= 1  
                # delete the the assignment of the already backtracked variable
                if current_variable in assignments:
                    del assignments[current_variable]  
                # add this sequence to visited so we don't visit again
                visited.add(tuple(current_sequence))
                # let the next iteration start from the next value in the previous layer
                current_domain_start_ind = current_sequence[-1] + 1
                # will start accepting new values from the prev layer started from current_domain_start_ind
                current_sequence.pop()
                print(f"-Backtracking to layer {current_layer}-")
                print(f"Popped: {current_domain_start_ind-1}")
                print(current_sequence)

        return list(assignments.values())

    def find_all_solutions_with_prints(self) -> list[list[subject]]:
        '''
        NB: contains print statements everywhere for debugging

        DP Backtracking Algorithm to get the ALl the possible Constraint-Satisfying TimeTable 

        :return: list of list of subjects, list of ALL possible TimeTables :)
        '''
        timetables_list = []

        no_more_timetables = False

        assignments: dict[str: subject] = {}  # the dictionary which maps each variable to correct value, sub_name to subject
        current_layer = 0  # the layer we are working on currently
        current_sequence = []  # It's a Stack! The path we moved through to get to current layer
        current_domain_start_ind = 0
        visited = set()  # set of tuple of correct sequence of domain indexes for each variable(sub_name+activity)
                             # will contain sequences that we know will get us to a dead-end 
                             # or that will get us to a timetable we already know

        while not no_more_timetables:
            
            while len(assignments) < len(self.variables):  # aka assignment dict doesn't still have all values assigned in it 

               current_variable = self.variables[current_layer]
               current_domain_values = self.domains[self.variables[current_layer]]

               print()
               print(current_variable, current_layer)

               for possible_value_ind, possible_value in enumerate(current_domain_values[current_domain_start_ind:]):

                   assignments[current_variable] = possible_value

                   current_sequence.append(current_domain_start_ind + possible_value_ind)

                   if self.consistent(current_variable, assignments) and tuple(current_sequence) not in visited:
                       # Found a potential new path
                       print(f"Adding: {current_domain_start_ind + possible_value_ind} out of {len(current_domain_values)}")
                       print(current_sequence)
                       current_layer += 1
                       current_domain_start_ind = 0
                       break

                   else:
                       # path tried doesn't satisfy constraints or already visited
                       current_sequence.pop()  
                       print(f"Skipping: {possible_value_ind} out of {len(current_domain_values)}")

               else:
                    # Reached a dead-end!
                    # Current Sequence have exhausted current layer's domain values

                    # If no value is right in the first layer, then no possible combination will work!
                    if current_layer == 0:
                        print("No More Timetables")
                        no_more_timetables = True
                        break

                    elif current_layer < 0:
                        raise ValueError("WTF?!??! HOW DID YOU REACH HERE?!??!")

                    ### Backtracking ###
                    # Go back one layer
                    current_layer -= 1  
                    # delete the the assignment of the already backtracked variable
                    if current_variable in assignments:
                        del assignments[current_variable]  
                    # add this sequence to visited so we don't visit again
                    visited.add(tuple(current_sequence))
                    # let the next iteration start from the next value in the previous layer
                    current_domain_start_ind = current_sequence[-1] + 1
                    # will start accepting new values from the prev layer started from current_domain_start_ind
                    current_sequence.pop()
                    print(f"-Backtracking to layer {current_layer}-")
                    print(f"Popped: {current_domain_start_ind-1}")
                    print(current_sequence)


            if no_more_timetables:
                break

            print()
            print()
            print("FOUND A TIMETABLE!!!!!!!!!!!!!!!!!!!!!!!!")
            timetables_list.append(list(assignments.values()))
            # Executing backtracking routine to continue as if we still didn't find a solution
            ### Backtracking ###
            # Go back one layer
            current_layer -= 1  
            # delete the the assignment of the already backtracked variable
            if current_variable in assignments:
                del assignments[current_variable]  
            # add this sequence to visited so we don't visit again
            visited.add(tuple(current_sequence))
            # let the next iteration start from the next value in the previous layer
            current_domain_start_ind = current_sequence[-1] + 1
            # will start accepting new values from the prev layer started from current_domain_start_ind
            current_sequence.pop()
            print(f"-Backtracking to layer {current_layer}-")
            print(f"Popped: {current_domain_start_ind-1}")
            print(current_sequence)


        return timetables_list

    def find_solution(self) -> list[subject]:
        '''
        DP Backtracking Algorithm to get the first Constraint-Satisfying TimeTable 

        :return: A list of subjects, A Valid TimeTable :)
        '''
        assignments: dict[str: subject] = {}  # the dictionary which maps each variable to correct value, sub_name to subject
        current_layer = 0  # the layer we are working on currently
        current_sequence = []  # It's a Stack! The path we moved through to get to current layer
        current_domain_start_ind = 0
        visited = set()  # set of tuple of correct sequence of domain indexes for each variable(sub_name+activity)
                         # will contain sequences that we know will get us to a dead-end 
                         # or that will get us to a timetable we already know

        while len(assignments) < len(self.variables):  # aka assignment dict doesn't still have all values assigned in it 

           current_variable = self.variables[current_layer]
           current_domain_values = self.domains[self.variables[current_layer]]

           for possible_value_ind, possible_value in enumerate(current_domain_values[current_domain_start_ind:]):

               assignments[current_variable] = possible_value

               current_sequence.append(current_domain_start_ind + possible_value_ind)

               if self.consistent(current_variable, assignments) and tuple(current_sequence) not in visited:
                   # Found a potential new path
                   current_layer += 1
                   current_domain_start_ind = 0
                   break

               else:
                   # path tried doesn't satisfy constraints or already visited
                   current_sequence.pop()  

           else:
                # Reached a dead-end!
                # Current Sequence have exhausted current layer's domain values

                # If no value is right in the first layer, then no possible combination will work!
                if current_layer == 0:
                    return None
                elif current_layer < 0:
                    raise ValueError("WTF?!??! HOW DID YOU REACH HERE?!??!")

                ### Backtracking ###
                # Go back one layer
                current_layer -= 1  
                # delete the the assignment of the already backtracked variable
                if current_variable in assignments:
                    del assignments[current_variable]  
                # add this sequence to visited so we don't visit again
                visited.add(tuple(current_sequence))
                # let the next iteration start from the next value in the previous layer
                current_domain_start_ind = current_sequence[-1] + 1
                # will start accepting new values from the prev layer started from current_domain_start_ind
                current_sequence.pop()

        return list(assignments.values())

    def find_all_solutions(self) -> list[list[subject]]:
        '''
        DP Backtracking Algorithm to get the ALl the possible Constraint-Satisfying TimeTable 

        :return: list of list of subjects, list of ALL possible TimeTables :)
        '''
        timetables_list = []

        no_more_timetables = False

        assignments: dict[str: subject] = {}  # the dictionary which maps each variable to correct value, sub_name to subject
        current_layer = 0  # the layer we are working on currently
        current_sequence = []  # It's a Stack! The path we moved through to get to current layer
        current_domain_start_ind = 0
        visited = set()  # set of tuple of correct sequence of domain indexes for each variable(sub_name+activity)
                             # will contain sequences that we know will get us to a dead-end 
                             # or that will get us to a timetable we already know

        while not no_more_timetables:
            
            while len(assignments) < len(self.variables):  # aka assignment dict doesn't still have all values assigned in it 

               current_variable = self.variables[current_layer]
               current_domain_values = self.domains[self.variables[current_layer]]


               for possible_value_ind, possible_value in enumerate(current_domain_values[current_domain_start_ind:]):

                   assignments[current_variable] = possible_value

                   current_sequence.append(current_domain_start_ind + possible_value_ind)

                   if self.consistent(current_variable, assignments) and tuple(current_sequence) not in visited:
                       # Found a potential new path
                       current_layer += 1
                       current_domain_start_ind = 0
                       break

                   else:
                       # path tried doesn't satisfy constraints or already visited
                       current_sequence.pop()  

               else:
                    # Reached a dead-end!
                    # Current Sequence have exhausted current layer's domain values

                    # If no value is right in the first layer, then no possible combination will work!
                    if current_layer == 0:
                        no_more_timetables = True
                        break

                    elif current_layer < 0:
                        raise ValueError("WTF?!??! HOW DID YOU REACH HERE?!??!")

                    ### Backtracking ###
                    # Go back one layer
                    current_layer -= 1  
                    # delete the the assignment of the already backtracked variable
                    if current_variable in assignments:
                        del assignments[current_variable]  
                    # add this sequence to visited so we don't visit again
                    visited.add(tuple(current_sequence))
                    # let the next iteration start from the next value in the previous layer
                    current_domain_start_ind = current_sequence[-1] + 1
                    # will start accepting new values from the prev layer started from current_domain_start_ind
                    current_sequence.pop()


            if no_more_timetables:
                break

            timetables_list.append(list(assignments.values()))
            # Executing backtracking routine to continue as if we still didn't find a solution
            ### Backtracking ###
            # Go back one layer
            current_layer -= 1  
            # delete the the assignment of the already backtracked variable
            if current_variable in assignments:
                del assignments[current_variable]  
            # add this sequence to visited so we don't visit again
            visited.add(tuple(current_sequence))
            # let the next iteration start from the next value in the previous layer
            current_domain_start_ind = current_sequence[-1] + 1
            # will start accepting new values from the prev layer started from current_domain_start_ind
            current_sequence.pop()


        return timetables_list


#TODO: make wrapper function to measure function performance time-wise
#TODO: make wrapper to save output to pickle file
def generateTimeTable(ALL_SUBJECTS: list[list[subject]], mode: Mode, *filters) -> list[subject]:
    '''
    Executing the CSP framework to generate a timetable

    :param mode: Mode Enum could be Normal or Debug. where Normal executes quietly without printing anything
                                                    Debug prints summary of results
    :param ALL_SUBJECTS: list of all possible subject objects for wanted subjects
    :param constraints: *arg argument where you can write as much 'Constraint' objects as you want to add to the CSP framework
    :return: list of subjects. AKA, a timetable
    '''

    # Creating CSP environment
    variables = get_variables(ALL_SUBJECTS)
    domains = get_domains(variables, ALL_SUBJECTS)

    # Creating CSP object
    csp = CSP(variables, domains)

    # Adding Constraints
    csp.add_constraint(DistinctTimesConstraint(variables))
    csp.add_constraint(SameSectionConstraint(variables))

    # Running backtracking DP Algorithm
    result = csp.find_solution()

    return result


#TODO: make wrapper function to measure function performance time-wise
#TODO: make wrapper to save output to pickle file
def generateTimeTables(ALL_SUBJECTS: list[list[subject]], mode: Mode, *constraints: list[Constraint]) -> list[list[subject]]:
    '''
    Executing the CSP framework to generate a timetable

    :param ALL_SUBJECTS: list of all possible subject objects for wanted subjects
    :param mode: Mode Enum could be Normal or Debug. where Normal executes quietly without printing anything
                                                    Debug prints summary of results
    :param constraints: *arg argument where you can write as much 'Constraint' objects as you want to add to the CSP framework
    :return: list of subjects. AKA, a timetable
    '''

    # Creating CSP environment
    variables = get_variables(ALL_SUBJECTS)
    domains = get_domains(variables, ALL_SUBJECTS)

    # Creating CSP object
    csp = CSP(variables, domains)

    # Adding Constraints
    csp.add_constraint(DistinctTimesConstraint(variables))  # This is a must constraint
    for constraint in constraints:
        csp.add_constraint(constraint(variables))

    # Running backtracking DP Algorithm
    results = csp.find_all_solutions()

    if mode == Mode.Debug:
        print(f"Number of Possible TimeTables: {len(results)}")

    return results



if __name__ == "__main__":

    # wanted_subjects = ["ECEN204", "MATH206", "ECEN203", "ECEN202", "ENTR301", "ENGL102"]

    # wanted_subs = ['CSCI205', 'CSCI112', 'HUMA102', 'MATH112']

    wanted_subs = ['ECEN311', 'ECEN313', 'HUMA002', 'ENGL102', 'ENTR301', 'MATH206', 'CHEM001']

    ALL_SUBJECTS = generateAllSublist(wanted_subs)

    result = generateTimeTables(ALL_SUBJECTS, SameSectionConstraint)
    print("Number of Possible TimeTables:", len(result))

    if result is not None:
        completeTest(wanted_subs, result)




