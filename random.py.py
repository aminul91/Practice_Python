import itertools

l1 = [1, 2, 3]
l2 = [10, 20, 30]
l3 = [100, 200, 300]

for i, j, k in itertools.product(l1, l2, l3):
    print(i, j, k)
    

for i, j in itertools.product(l1, l2):
    print(i, j)
