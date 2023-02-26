from operator import mul
from functools import reduce

# lista = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

ranges=((1, 4), (0, 3), (3, 6))
operations = reduce(mul,(p[1]-p[0] for p in ranges)) - 1  # calculating how many times the while loop will run
# print(operations)
result = [i[0] for i in ranges]
print(result)
pos = len(ranges)-1
increments = 0
while increments < operations:
    # print("done")
    if result[pos] == ranges[pos][1]-1:
        # print(result[pos])
        # print(ranges[pos][1]-1)
        result[pos] = ranges[pos][0]
        pos -= 1
        print(result, "here")
    else:
        result[pos] += 1
        increments += 1
        pos = len(ranges)-1 #increment the innermost loop
        print(result)

