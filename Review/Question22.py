def create_matrix(filename):
    with open(filename) as file:
        alist = file.readlines()
    for i in range(len(alist)):
        alist[i] = list(alist[i].rstrip().split())

    return alist

import json
my_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
my_json = json.dumps(my_dict)
print(type(my_json))

for anInt in '647':
    anInt = anInt + 1



