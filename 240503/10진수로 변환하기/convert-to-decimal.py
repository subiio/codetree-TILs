n = (input())
n = list(n)
num = 0
for i in range(len(n)-1,-1,-1):
    num += int(n[i])*2**abs(i-4)
   
print(num)