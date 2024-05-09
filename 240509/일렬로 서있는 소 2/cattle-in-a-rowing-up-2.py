N = int(input())

hei = list(map(int,input().split()))
count =0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if hei[i] <= hei[j] <= hei[k]:
                count += 1

print(count)