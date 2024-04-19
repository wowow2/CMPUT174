file = open("ins.txt", "r")
lines = file.readlines()
for line in lines:
    strings = line.split()
    name = strings[0]
    sections = ",".join(strings[1:])
    print(f"{name} is a CMPUT 174 instructor for sections {sections}")
file.close()