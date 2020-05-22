list1 = list(map(int, input().strip().split()))
list2 = list(map(int, input().strip().split()))
print(list(set(list1).intersection(set(list2))))
