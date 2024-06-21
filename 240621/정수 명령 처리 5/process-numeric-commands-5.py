N = int(input())

list1 = []
for i in range(N):
    command = input()
    try:
        comm,key = command.split()
    except:
        comm = command
    if comm == "push_back":
        list1.append(key)
    elif comm == "get":
        print(list1[int(key)-1])
    
    elif comm == "size":
        print(len(list1))
    else:
        list1.pop()