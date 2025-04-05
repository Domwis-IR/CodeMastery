def solveNQueen(n):
    count = 0
    # rows: 해당 행에 퀸이 놓였는지 체크
    rows = [False] * n
    # diag1: (row - col + n - 1) 인덱스로 주대각선 체크
    diag1 = [False] * (2 * n - 1)
    # diag2: (row + col) 인덱스로 부대각선 체크
    diag2 = [False] * (2 * n - 1)

    def backtrack(col):
        nonlocal count
        # 모든 열에 퀸을 배치했다면 해를 찾은 것
        if col == n:
            count += 1
            return
        for row in range(n):
            if not rows[row] and not diag1[row - col + n - 1] and not diag2[row + col]:
                # 현재 (row, col)에 퀸을 배치 가능한 경우 표시
                rows[row] = True
                diag1[row - col + n - 1] = True
                diag2[row + col] = True

                backtrack(col + 1)

                # 배치 취소 (백트래킹)
                rows[row] = False
                diag1[row - col + n - 1] = False
                diag2[row + col] = False

    backtrack(0)
    return count

# 예시 실행: 8-Queen 문제의 해의 개수를 출력

N = int(input())
print(solveNQueen(N))
