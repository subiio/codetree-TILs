n = input()
n = int(n)
list1 = [1]

list1.append(n)
a = True
i = 2
while a== True:
    list1.append(list1[i-1]+list1[i-2])
    number = list1[i-1] + list1[i-2]
    i += 1
    if number >= 100:
        a = False
    
for i in (list1):
    print(i,end=' ')