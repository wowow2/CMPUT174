
output = ''
for i in range(2000, 2501):
    if (i % 5 != 0) and (i % 7 == 0):
        output += f'{i},'
print(output.rstrip(','))
