def mult(x, y):
    result = []
    for i in range(min(len(x), len(y))):
        result.append(x[i] * y[i])
    return tuple(result)

tup1 = (4, 2, 2, 2,-1,18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

print(mult(tup1, tup2))
