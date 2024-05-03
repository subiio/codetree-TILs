m1,d1,m2,d2 = map(int,input().split())

months_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

total_days_later = 0
total_days_start = 0
for i in range(1,m2):
    total_days_later += months_day[i]

total_days_later += d2

for j in range(1,m1):
    total_days_start += months_day[j]

total_days_start += d1

print(total_days_later-total_days_start+1)