years = int(input())

price_list = list(map(int,input().split()))

difference_list = []
for i in range(years):
    for j in range(i+1,years):
        difference_list.append(price_list[j]-price_list[i])

print(max(difference_list))