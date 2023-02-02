from operator import add
from numpy import product

# lista = [(1, 2, 3, 4, 5), (6, 7, 8), (9, 10, 11, 12)]
listb = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

operations = product([len(i) for i in listb]) - 1
print(operations)
result = [i[0] for i in listb]
print(result)
pos = len(listb) -1
increments = 0

while increments < operations:
    # print("done")
    if result[pos] == listb[pos][-1]:
        # print(result[pos])
        # print(listb[pos][1]-1)
        result[pos] = listb[pos][0]
        pos -= 1
        # break
    else:
        # must know where i am in the loop and  increment the value that is supposed to be incremented
        # result[pos] = listb[pos][(increments - (increments//3)*3) - 1]  # get the next value of listb[pos]
        result[pos] += 1
        print(result[pos], "here")
        x = listb[pos][-1]  # must make x equal to the value of (result[pos] += 1)
        print(x, "here2")
        increments += 1
        pos = len(listb) - 1  # increment the innermost loop
        print(result)
