m1,d1,m2,d2 = map(int,input().split())

relative = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']


month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

total_days_start = 0
total_days_later = 0
for i in range(1,m1):
    total_days_start += month_days[i]
total_days_start += d1

for j in range(1,m2):
    total_days_later += month_days[j]
total_days_later += d2

days_difference = total_days_later-total_days_start

print(relative[days_difference%7])