alphabet = 'abcdefghijklmnopqrstuvwxyz'
orig_list = ['bat', 'act', 'cat', 'rat', 'abs']
def remove_words(orig_list):
    new_list = []
    for i in range(len(orig_list)):
        flag = True
        for j in range(len(orig_list[i])):
            if orig_list[i][j] == alphabet[j]:
                flag = False
        if flag:
            new_list.append(orig_list[i])
    return new_list

new_list = remove_words(orig_list)
print(new_list)