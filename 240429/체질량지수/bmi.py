h,w = map(int,input().split())
bmi = w/((h/100)**2)

if bmi >= 25:
    print(int(bmi))
    print("Obesity")
else:
    print(int(bmi))