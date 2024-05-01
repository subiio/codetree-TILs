N = input()
N = int(N)

list1 = list(map(int,input().split()))

list2 = sorted(list1,reverse=True)
print(list2[0],list2[1])