string = ''
input_list = []
movies = []

while string != "END":
    string = input("")
    if string != "END":
        input_list.append(string.split(','))

actor = input('')
for i in range(len(input_list)):
    for j in range(len(input_list[i])):
        if input_list[i][j] == actor:
            movies.append(input_list[i][0])

for i in range(len(movies)):
    print(movies[i])


