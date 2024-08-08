n, m = map(int, input().split())
suyeol = []
for _ in range(n):
    suyeol.append(list(map(int, input().split())))


def count_numbers(a, m):
    count_dict = {}
    for num in a:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num, count in count_dict.items():
        if count >= m:
            return True
    return False


# 열 추가하기
for i in range(n):
    col = []
    for j in range(n):
        col.append(suyeol[j][i])
    suyeol.append(col)

count = 0
for row in suyeol:
    if count_numbers(row, m):
        count += 1

print(count)