list1 = list(map(int,input().split()))

list2 = []
list3 = []

for i in list1:
    if i > 500 :
        list2.append(i)
    else:
        list3.append(i)
    
print(max(list3),min(list2))