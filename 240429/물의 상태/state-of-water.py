tempWater = int(input())

if tempWater < 0:
    print("ice")
elif tempWater >= 100:
    print("vapor")
else:
    print("water")