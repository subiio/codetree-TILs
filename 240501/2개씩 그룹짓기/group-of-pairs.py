N = int(input())

list1 = list(map(int,input().split()))
list1 = sorted(list1)

list2 = []
if N == 1:
    print(sum(list1))
else:
    for i in range(N):
        list2.append(list1[i] + list1[2*N-1-i])

    print(max(list2))