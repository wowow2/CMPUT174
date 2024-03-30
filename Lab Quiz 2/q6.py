file = open("nutrition.txt", 'r')
f = file.readlines()
new_list = []
values = []
names = []
nut = input("")

for i in range(len(f)):
    line_list = f[i].rstrip().split(',')
    new_list.append(line_list)

for i in range(len(new_list)):
    for j in range(len(new_list[i])):
        if nut == new_list[i][j]:
            index = j
    values.append(new_list[i][index])
    names.append(new_list[i][0])

values = values[1:]
names = names[1:]

max_value = max(values)
answer = names[values.index(max_value)]

print(answer)

