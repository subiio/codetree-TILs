N = input()
N = int(N)

list1 = list(map(int,input().split()))

tmp = 100

for i in list1:
    if i < tmp:
        tmp = i

count = 0
for j in range(N):
    if list1[j] == tmp:
        count += 1
    else:
        pass

print(tmp, count)