import sys
from itertools import combinations

input = sys.stdin.readline

# 1. 입력 및 치킨집, 집 좌표 저장
N, M = map(int, input().split())
houses = []        # 집 좌표 리스트
chicken_shops = [] # 치킨집 좌표 리스트

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:      # 집이면
            houses.append((i, j))
        elif row[j] == 2:    # 치킨집이면
            chicken_shops.append((i, j))

# 거리 계산 함수 (맨해튼 거리)
def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

min_total_distance = float('inf')  # 최소 총 치킨 거리를 저장할 변수

# 2. 가능한 치킨집 M개 조합을 모두 탐색
for selected in combinations(chicken_shops, M):
    total_distance = 0
    # 각 집마다 가장 가까운 치킨집과의 거리를 계산
    for house in houses:
        # 선택된 치킨집 조합 내에서 house와의 거리를 리스트에 저장한 후 최소값 취함
        distances = [get_distance(house, chicken) for chicken in selected]
        total_distance += min(distances)
    # 최소 치킨 거리를 갱신
    if total_distance < min_total_distance:
        min_total_distance = total_distance

# 3. 결과 출력
print(min_total_distance)
