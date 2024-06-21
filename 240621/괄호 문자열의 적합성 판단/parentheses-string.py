stack_list = []

huhuh = input()
answer = None
for _ , value in enumerate(huhuh):
    if value == '(':
        stack_list.append(value)
    else:
        if len(stack_list) == 0 :
            answer = "No"
            print(answer)
            break
        stack_list.pop()

if answer == None:
    if len(stack_list) == 0:
        print("Yes")
    else:
        print("No")