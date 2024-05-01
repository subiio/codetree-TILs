list1 = list(map(int,input().split()))
tmp = 0

for i in list1:
    if i > tmp:
        tmp = i

print(tmp)