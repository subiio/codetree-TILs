a,b,c,d = map(int,input().split())
total_time_later = 60*c + d
total_time_start = 60*a + b

print(total_time_later-total_time_start)