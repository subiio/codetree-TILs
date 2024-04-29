n = int(input())
list1 = list(map(int,input().split()))
list2 = [i*i for i in list1]
for i in list2:
    print(i,end = ' ')