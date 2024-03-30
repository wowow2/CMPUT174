grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
grid_T = list(map(list, zip(*grid)))

print(grid)
print(list(zip(*grid)))
