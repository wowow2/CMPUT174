def print_file(filename):
    f = open(filename, 'r')
    content = f.readlines()
    f.close()
    for line in content:
        print(line.rstrip())
print_file('names.txt')