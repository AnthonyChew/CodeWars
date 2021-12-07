def create_multiplications(n):

    res = []

    for i in range(n):
        res += [lambda x , i = i : x * i]
    return res


for m in create_multiplications(3):
    print(m(3), ' ... ')
