a = list(input())
# print(a)
# TODO
def calculate_run_length(a):
    # 초기 length
    length = 2
    prev_string = a[0]
    count = 0
    for i in a:
        if prev_string != i:
            length += 2
            count += 1
            prev_string = i
        else:
            pass
    if count == 0 :
        length = 3
        return length
    else:
        return length



# TODO
def rotate(a):
    b = []
    tmp = a[-1]
    b.append(tmp)
    for i in range(0,len(a)-1):
        b.append(a[i])
    # print(b)
    return b




min_length = []
b = calculate_run_length(a)
min_length.append(b)
for _ in range(len(a)-1):
    a = rotate(a)
    b = calculate_run_length(a)
    min_length.append(b)

print(min(min_length))