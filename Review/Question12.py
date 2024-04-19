d1 = {'a':100, 'b':200, 'c':300}
d2 = {'a':300, 'b':200, 'd':400}
combine_dict = {}

for k1, v1 in d1.items():
    combine_dict[k1] = v1

for k2, v2 in d2.items():
    if k2 in combine_dict:
        combine_dict[k2] = combine_dict[k2] + v2
    else:
        combine_dict[k2] = v2

print(len('123'))