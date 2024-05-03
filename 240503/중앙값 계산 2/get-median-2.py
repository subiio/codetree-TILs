n = int(input())

list1 = list(map(int,input().split()))


def find_center(num_list):
    a = sorted(num_list)
    lens = len(a)
    return num_list[lens//2]
list2 = []
for i in range(len(list1)):
    list2.append(list1[i])
    if i%2 == 0:
        print(find_center(list2), end = ' ')