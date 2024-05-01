n = input()
n = int(n)
count = 0
baesu = 1
list2 = []
while count != 2:
    a =n * baesu
    list2.append(a)
    if a%5 == 0:
        count += 1
    baesu += 1
    
for i in list2:
    print(i, end = ' ')