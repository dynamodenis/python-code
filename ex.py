# import pdb; pdb.set_trace()
a = [1, 2, 3]
b = [7, 8, 9]

print([(x + y) for (x,y) in zip(a,b)])