def max_non_overlapping_segments(segments):
    # 선분을 오른쪽 끝점 기준으로 정렬합니다.
    segments.sort(key=lambda x: x[1])
    
    n = len(segments)
    dp = [0] * n
    
    # 모든 선분에 대해 DP를 초기화합니다.
    for i in range(n):
        dp[i] = 1  # 최소한 자신만 포함된 경우
    
    # DP 테이블을 채웁니다.
    for i in range(n):
        for j in range(i):
            if segments[j][1] < segments[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # DP 테이블에서 최대 값을 찾습니다.
    return max(dp)

# 입력 처리
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
segments = []

for i in range(n):
    x1 = int(data[2 * i + 1])
    x2 = int(data[2 * i + 2])
    segments.append((x1, x2))

# 결과 출력
print(max_non_overlapping_segments(segments))