brackets = input()
S = 0
for i in range(len(brackets)):
    if brackets[i] == ')':
        continue
    for j in range(i+1,len(brackets)):
        if brackets[j] == ')':
            S += 1

print(S)