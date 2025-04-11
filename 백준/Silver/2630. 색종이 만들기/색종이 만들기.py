n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
result = []

def solution(x,y,n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 해당영역에서 하나라도 색이 다르다면 1/2씩 쪼개서 들어감
            if paper[i][j] != color:
                solution(x,y,n//2)
                solution(x,y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                # 해당 구역들 다 돌았으니 return
                return
    # 해당구역에서 걸린부분 없으니 모두 같은 색
    # 색에 따라서 0,1 부여, 결과 리스트에 추가 
    if color == 0:
        result.append(0)
    else :
        result.append(1)

solution(0,0,n)
# 결과 리스트에 들어있는 수를 셈으로써 몇 개의 종이인지를 count 해줄 수 있음.
print(result.count(0))
print(result.count(1))
