def multiples(lst, n):
    new_lst = []
    for i in range(len(lst)):
        if lst[i] % n == 0:
            new_lst.append(lst[i])
    return new_lst


# Do not touch
def main():
  theList = list(map(lambda x: int(x), input().split()))
  n = int(input())
  print(" ".join(map(lambda x: str(x), multiples(theList, n))))
  print(" ".join(map(lambda x: str(x), theList)))

main()