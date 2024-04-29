numbers = list(map(int,input().split()))
sum = 0
count = 0
for i in range(len(numbers)):
    if 1<= numbers[i] < 250:
        sum += numbers[i]
        count += 1
    else:
        break
print("%d %.1f" %(sum,count))