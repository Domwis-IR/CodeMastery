import sys
from itertools import combinations

input = sys.stdin.readline

# 1. 입력 및 집, 치킨집 좌표 저장
N, M = map(int, input().split())
houses = []
chickens = []

for i in range(N):
    row = list(map(int, input().split()))
    for j, value in enumerate(row):
        if value == 1:
            houses.append((i, j))
        elif value == 2:
            chickens.append((i, j))

# 2. 사전 계산: 각 집에서 각 치킨집까지의 맨해튼 거리를 미리 계산
# dist_matrix[i][j]는 i번째 집에서 j번째 치킨집까지의 거리
dist_matrix = [
    [abs(hx - cx) + abs(hy - cy) for cx, cy in chickens]
    for hx, hy in houses
]

min_total_distance = float('inf')
# 3. 치킨집 인덱스 조합을 선택하여 각 집의 최소 거리 합을 계산 (조기 종료 포함)
for comb in combinations(range(len(chickens)), M):
    total_distance = 0
    for i in range(len(houses)):
        # 조합에 속한 치킨집 중, i번째 집에 대한 최소 거리를 찾는다.
        min_distance = float('inf')
        for c in comb:
            if dist_matrix[i][c] < min_distance:
                min_distance = dist_matrix[i][c]
        total_distance += min_distance
        # 현재까지의 총합이 이미 최적값 이상이면 더 이상 계산할 필요 없음
        if total_distance >= min_total_distance:
            break
    if total_distance < min_total_distance:
        min_total_distance = total_distance

# 4. 결과 출력
print(min_total_distance)
