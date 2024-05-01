years = int(input())

price_list = list(map(int,input().split()))

difference_list = []
if years == 1:
    print(0)
else:
    for i in range(years):
        for j in range(i+1,years):
            difference_list.append(price_list[j]-price_list[i])

if max(difference_list) > 0:
    print(max(difference_list))
else:
    print(0)