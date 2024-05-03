a,b,c = map(int,input().split())
start_a = 11
start_b = 11
start_c = 11
time_total = 0
while True:
    if (start_a,start_b,start_c) > (a,b,c):
        print(-1)
        break 
    if start_a == a and start_b == b and start_c == c:
        break
    time_total += 1
    start_c += 1
    if start_c == 60:
        start_c = 0
        start_b += 1
    if start_b == 24:
        start_b = 0
        start_a += 1

print(time_total)