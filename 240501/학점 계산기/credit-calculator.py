sub = int(input())
score = list(map(float,input().split()))
average = sum(score)/(sub)

if average >= 4.0:
    print("%.1f" %(average))
    print("Perfect")
elif 3.0<= average < 4.0:
    print("%.1f" %(average))
    print("Good")
else:
    print("%.1f" %(average))
    print("Poor")