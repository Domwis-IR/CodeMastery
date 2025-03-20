from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    answer = bfs(maps, n, m) 
    
    return answer if answer else -1

def bfs(grid, n, m):
    direction = [(1,0), (-1,0), (0,1), (0,-1)]
    
    visited = [[False] * m for _ in range(n)]
    routes = [[0] * m for _ in range(n)]
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    routes[0][0] = 1
    while q:
        x, y = q.popleft()
        
        if x == n-1 and y == m-1:
            return routes[x][y]
        
        for i in range(4):
            dx, dy = x + direction[i][0], y + direction[i][1]
            if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] == 1:
                if not visited[dx][dy]:
                    routes[dx][dy] = routes[x][y] + 1
                    visited[dx][dy] = True
                    q.append((dx, dy))
    return routes[-1][-1]
                    
                    
                    
                    