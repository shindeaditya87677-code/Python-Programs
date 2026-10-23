#program to find cube using map function
numbers = [2, 4, 6, 7, 9, 8]

cube = list(map(lambda x: x*x*x, numbers))

print(cube)