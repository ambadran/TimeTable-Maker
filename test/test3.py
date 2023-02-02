
resistances = [0.68, 0.82, 1, 1.5, 2.2, 4.7, 10]
capacitances = [100, 220, 330, 470, 1000, 2200, 4700]

for i in resistances:
    for n in capacitances:
        if i*n > 800 and i*n <950:
            print("first")
            print(i, n, i*n)
            print((i*n)/60)

for i in resistances:
    for n in capacitances:
        if i*n > 1100 and i*n <1500:
            print("second")
            print(i, n, i*n)
            print((i*n)/60)