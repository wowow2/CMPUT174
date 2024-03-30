# q1.py

'''
Title: Question 1
Author: Abbas Rizvi
Date: 2024/03/09
'''

# open the file then readlines
file = open('numbers.txt', 'r')
f = file.readlines()
file.close()
int_list = []

# iterate through list and remove /n and split alongside white spaces
for line in f:
    line_list = line.split()
    for line1 in line_list:
        # append numbers from each line in new list
        int_list.append(int(line1))


int_list = sorted(int_list) # sort list from least to greatest used sorted
total = sum(int_list) # use sum(list) to get total of the list
n = len(int_list)

if n % 2 != 0:
    median = int_list[int((n+1)/2)-1] # list length is even then median is index [length of the list plus one divided by 2, then subtract 1]
else:
    median = (int_list[int(n/2-1)]+int_list[int(n/2)])/2 # list length is odd then median is index[legnth of the list divided by 2,then subtact 1]

mean = total / len(int_list) # mean is total divded by length

print(f'{mean:.2f} {median:.1f}') # 2.f and 1.f signify decimal places

