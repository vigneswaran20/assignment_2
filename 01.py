x = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

y = []
z = []

for i in x:
    y.append(i[1],)

y.sort()

for i in y:
    for j in x:
        if i == int(j[1],):
            z.append(j)

print(z)


