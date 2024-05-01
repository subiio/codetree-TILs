n = input()
n = int(n)

list1 = list(map(int,input().split()))
list2 =[]
for _ in range(n):
    a = list1.pop()
    if a%2 == 0:
        list2.append(a)
    else:
        pass

for i in list2:
    print(i,end = ' ')