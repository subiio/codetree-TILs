# a = input().split()
# i = len(a)
# while i != 0:
#     i -= 1
#     print(a[i],end='')


a = list(map(int,input().split()))

i=len(a)
for i in range(len(a)-1,-1,-1):
    print(a[i],end='')