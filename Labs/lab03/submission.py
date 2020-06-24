## import modules here
import numpy as np
################# Question 1 #################

def hc(data, k):# do not change the heading of the function
    sim_matrix = {}
    maxval = -1
    maxpos = None
    for i in range(len(data)):
        if not i:
            continue

        sim_matrix[f'{i}'] = {}

        for j in range(i + 1):
            if i != j:
                d = dot_product(data[i], data[j])

                if d > maxval:
                    maxval = d
                    maxpos = f'{i}', f'{j}'

                sim_matrix[f'{i}'][f'{j}'] = d

    if k >= len(data):
        return [i for i in range(len(data))]

    while True:
        clusters = list(sim_matrix[list(sim_matrix.keys())[0]]) + list(sim_matrix.keys())

        if k == len(clusters):
            labels = [-1] * len(data)
            ctr = 0

            for i in clusters:
                for j in i.split(','):
                    labels[int(j)] = ctr

                ctr += 1

            break

        x = clusters[min(clusters.index(maxpos[0]), clusters.index(maxpos[1]))]
        y = clusters[max(clusters.index(maxpos[0]), clusters.index(maxpos[1]))]

        for key in clusters:
            if clusters.index(key) < clusters.index(x):
                sim_matrix[x][key] = min(sim_matrix[x][key], sim_matrix[y][key])
            elif clusters.index(x) < clusters.index(key) < clusters.index(y):
                sim_matrix[key][x] = min(sim_matrix[key][x], sim_matrix[y][key])
            elif clusters.index(key) > clusters.index(y):
                sim_matrix[key][x] = min(sim_matrix[key][x], sim_matrix[key][y])

        temp1 = {}
        maxval = -1
        maxpos = None
        for key1, val1 in sim_matrix.items():
            if key1 == y:
                continue

            if key1 == x:
                temp1[f'{x},{y}'] = val1

                for key2, val2 in val1.items():
                    if val2 > maxval:
                        maxval = val2
                        maxpos = f'{x},{y}', key2
            else:
                temp2 = {}

                for key2, val2 in val1.items():
                    if key2 == y:
                        continue

                    if key2 == x:
                        temp2[f'{x},{y}'] = val2

                        if val2 > maxval:
                            maxval = val2
                            maxpos = key1, f'{x},{y}'
                    else:
                        temp2[key2] = val2

                        if val2 > maxval:
                            maxval = val2
                            maxpos = key1, key2

                temp1[key1] = temp2

        sim_matrix = dict(temp1)

    return labels

def dot_product(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res
