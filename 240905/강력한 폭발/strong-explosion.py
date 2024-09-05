from itertools import product

def apply_bomb(grid, x, y, bomb_type):
    directions = [
        [(-2,0), (-1,0), (0,0), (1,0), (2,0)], # T형 폭탄
        [(-1,0), (1,0), (0,0), (0,1), (0,-1)], # +형 폭탄
        [(-1,-1), (-1,1), (0,0), (1,1), (1,-1)] # X형 폭탄
    ]
    
    affected = set()
    for dx, dy in directions[bomb_type]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            affected.add((nx, ny))
    return affected

def count_destroyed_area(grid, bombs):
    affected_area = set()
    for (x, y, bomb_type) in bombs:
        affected_area.update(apply_bomb(grid, x, y, bomb_type))
    return len(affected_area)

def get_max_destroyed_area(grid, bomb_positions):
    max_destroyed = 0
    bomb_types = len(explode_list) # Number of bomb types
    
    # 모든 폭탄 배치 조합을 시도
    for combination in product(range(bomb_types), repeat=len(bomb_positions)):
        bombs = [(bomb_positions[i][0], bomb_positions[i][1], combination[i]) for i in range(len(bomb_positions))]
        max_destroyed = max(max_destroyed, count_destroyed_area(grid, bombs))
    
    return max_destroyed

# 입력 처리
n = int(input().strip())
grid = [list(map(int, input().strip().split())) for _ in range(n)]

# 폭탄 위치 수집
bomb_positions = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]

# 폭탄 유형 정의
explode_list = [[(-2,0), (-1,0), (0,0), (1,0), (2,0)], # T형 폭탄
                [(-1,0), (1,0), (0,0), (0,1), (0,-1)], # +형 폭탄
                [(-1,-1), (-1,1), (0,0), (1,1), (1,-1)]] # X형 폭탄

# 최대 초토화 영역 수 계산
print(get_max_destroyed_area(grid, bomb_positions))