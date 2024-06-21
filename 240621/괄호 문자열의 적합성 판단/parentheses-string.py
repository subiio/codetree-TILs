stack_list = []

huhuh = input()

for _ , value in enumerate(huhuh):
    if value == '(':
        stack_list.append(value)
    else:
        if len(stack_list) == 0 :
            print("No")
            break
        stack_list.pop()

if len(stack_list) == 0:
    print("Yes")
else:
    print("No")