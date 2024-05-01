n = input()
n = int(n)
pf = []

count = 0
for _ in range(n):
    list1 = list(map(int,input().split()))
    ave = sum(list1)/len(list1)
    if ave >= 60:
        print("pass")
        pf.append("pass")
        count += 1
    else:
        print("fail")
        pf.append("fail")
print(count)