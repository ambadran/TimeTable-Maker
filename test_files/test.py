
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

            print(current_variable, current_layer) # FOR DEBUGGING
            
            for possible_value_ind in range(last_possible_value_ind, len(current_domain)):

                assignments[current_variable] = current_domain[possible_value_ind]

                last_possible_value_inds[current_layer] = possible_value_ind
                print(possible_value_ind, len(current_domain)) # FOR DEBUGGING

                if self.consistent(current_variable, assignments) and tuple(last_possible_value_inds) not in visited:

                    print(last_possible_value_inds) # FOR DEBUGGING

                    current_layer += 1

                    break
                else:
                    visited.add(tuple(last_possible_value_inds))
            else:
                # no value in this layer is consistent with current combination of values in assignments dict
                # Thus, backtracking

                print('backtracking') # FOR DEBUGGING

                if current_variable in assignments:
                    del assignments[current_variable]

                visited.add(tuple(last_possible_value_inds))  #TODO: try type casting to tuple, maybe will be faster

                last_possible_value_inds[current_layer] = 0

                current_layer -= 1

                last_possible_value_inds[current_layer] += 1

                print(last_possible_value_inds) # FOR DEBUGGING

                if current_layer == -1:
                    possible_time_table_to_be_found = False
                    return None # No possible timetable found

        timetable = list(assignments.values())
        for sub in timetable:
            print(sub.name, sub.section, sub.times) # FOR DEBUGGING

        return timetable

    def find_all_solutions(self) -> list[list[subject]]:
        '''
        DP Algorithm to find every possible solution to this CSP

        :return : list of list of subjects, list of subjects which satisfy constraints, aka list of TimeTables :)

        exact same algorithm as find_first_solution but now whenever it finds a correct timetable,
        it just adds it to visited set
        '''

        timetables: list[list[subject]] = []  # will contain list of timetables

        last_possible_value_inds = [0 for _ in range(len(self.variables))]

        visited = set()

        possible_time_table_to_be_found = True

        while possible_time_table_to_be_found:

            assignments = {}

            current_layer = 0

            while len(assignments) < len(self.variables):

                current_variable = self.variables[current_layer]
                current_domain = self.domains[current_variable]

                last_possible_value_ind = last_possible_value_inds[current_layer]

                print(current_variable, current_layer) # FOR DEBUGGING
                
                for possible_value_ind in range(last_possible_value_ind, len(current_domain)):

                    assignments[current_variable] = current_domain[possible_value_ind]

                    last_possible_value_inds[current_layer] = possible_value_ind
                    print(possible_value_ind, len(current_domain)) # FOR DEBUGGING

                    if self.consistent(current_variable, assignments) and tuple(last_possible_value_inds) not in visited:

                        print(last_possible_value_inds) # FOR DEBUGGING

                        current_layer += 1

                        break
                    else:
                        print(self.consistent(current_variable, assignments), 'first')
                        print(tuple(last_possible_value_inds) not in visited, 'second')
                        visited.add(tuple(last_possible_value_inds))

                else:
                    # no value in this layer is consistent with current combination of values in assignments dict
                    # Thus, backtracking

                    # first delete prev element
                    if current_variable in assignments:
                        del assignments[current_variable]

                    ### Backtracking
                    # resetting the current layer to be visited again and tried for all it's domain values but
                    # with a different previous element combination
                    last_possible_value_inds[current_layer] = 0  
                    
                    current_layer -= 1  # backtrack once
                    print(f'Backtracking to layer{current_layer}') # FOR DEBUGGING
                    print(last_possible_value_inds) # FOR DEBUGGING
                    while last_possible_value_inds[current_layer] == len(self.domains[self.variables[current_layer]]) - 1:
                        # keep backtracking if previous layer is in it's last possible domain element
                        last_possible_value_inds[current_layer] = 0  # but first zero out this completed layer
                        current_layer -= 1  # then backtrack again
                        print(f'Backtracking to layer{current_layer}') # FOR DEBUGGING
                        print(last_possible_value_inds) # FOR DEBUGGING


                    last_possible_value_inds[current_layer] += 1  # next time start searching from the next position


                    if current_layer < 0:
                        possible_time_table_to_be_found = False
                        break

            timetables.append(list(assignments.values()))
            visited.add(tuple(last_possible_value_inds))
            print('New TimeTable Found!')
            for sub in timetables[-1]:
                print(sub.name, sub.section, sub.times) # FOR DEBUGGING
            print()
            print()
            print()

        return timetables


