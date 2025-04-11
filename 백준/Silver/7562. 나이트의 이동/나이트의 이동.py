t = int(input())
d = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

from collections import deque
def bfs(start):
    q = deque()
    q.append(start)
    while q:
        start_ = q.popleft()
        if start_ == end:
            return visited[start_[0]][start_[1]] - 1
        for i in d:
            dx = start_[0] + i[0]
            dy = start_[1] + i[1]
            if 0 <= dx < n and 0 <= dy < n:
                if not visited[dx][dy]:
                    visited[dx][dy] = visited[start_[0]][start_[1]] + 1
                    q.append([dx,dy])         

for _ in range(t):
    n = int(input())
    visited = [[0] *n for _ in range(n)]
    start = list(map(int,input().split()))
    visited[start[0]][start[1]] = 1
    end = list(map(int,input().split()))
    print(bfs(start))
    
# 경로를 지나가면서 횟수를 셀 경우 DFS가 아니라 BFS로 접근해야한다.
