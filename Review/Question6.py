def remove_zeros(alist):
    new_list = []
    for num in alist:
        if num != 0:
            new_list.append(num)
    return new_list

x = remove_zeros([78,0,90,67,5,34,0,45,98,0,78,0])
print(x)