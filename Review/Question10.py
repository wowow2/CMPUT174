def zip(keys, values):
    Dict = {}
    for i in range(len(keys)):
        Dict[keys[i]] = values[i]
    return Dict


print(zip(['Ten','Twenty','Thirty'],[10, 20, 30]))
#{'Ten':10,'Twenty':20, 'Thirty':30}