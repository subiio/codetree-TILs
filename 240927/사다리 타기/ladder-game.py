import copy

# 입력 받기
n, m = map(int, input().split())
ladder_list = [list(map(int, input().split())) for _ in range(m)]

# 초기 사다리 상태 설정
init_number_list = list(range(1, n+1))

# 사다리 타기 동작 함수
def ladder_tagi(number_list, ladder):
    # 깊은 복사를 줄이기 위해 바로 결과를 변환
    for a, b in sorted(ladder, key=lambda x: x[1]):
        number_list[a-1], number_list[a] = number_list[a], number_list[a-1]
    return number_list

# 최소 가로줄 수를 찾기 위한 백트래킹
def backtracking(idx, current_ladder, final_ladder):
    global min_len

    # 종료 조건: 결과가 같아진 경우
    if ladder_tagi(copy.deepcopy(init_number_list), current_ladder) == final_ladder:
        min_len = min(min_len, len(current_ladder))
        return

    # 백트래킹 수행
    for i in range(idx, m):
        current_ladder.append(ladder_list[i])
        backtracking(i + 1, current_ladder, final_ladder)
        current_ladder.pop()

# 초기 상태와 최종 목표 상태 계산
end_grid = ladder_tagi(copy.deepcopy(init_number_list), ladder_list)

# 최소 가로줄의 수를 저장하는 변수
min_len = float('inf')

# 백트래킹 수행
backtracking(0, [], end_grid)

# 결과 출력
print(min_len)