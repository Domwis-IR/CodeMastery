def solve_sudoku(board):
    """
    board: 9x9 리스트 (리스트의 리스트)로, 0은 빈 칸을 의미.
    스도쿠 문제를 백트래킹으로 풀고, 완성된 board를 반환한다.
    """
    # 9x10 크기의 불리언 배열 (인덱스 1~9 사용, 0번은 사용하지 않음)
    rows = [[False] * 10 for _ in range(9)]
    cols = [[False] * 10 for _ in range(9)]
    blocks = [[False] * 10 for _ in range(9)]
    
    # 빈 칸의 위치를 미리 저장 (i, j) 튜플 리스트
    empty_cells = []
    
    # 초기 board 상태에 맞춰 rows, cols, blocks를 세팅
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == 0:
                empty_cells.append((i, j))
            else:
                rows[i][num] = True
                cols[j][num] = True
                block_index = (i // 3) * 3 + (j // 3)
                blocks[block_index][num] = True

    def backtrack(idx):
        # 모든 빈 칸을 채웠다면 스도쿠 완성 → 종료 조건
        if idx == len(empty_cells):
            return True

        i, j = empty_cells[idx]
        block_index = (i // 3) * 3 + (j // 3)
        
        for num in range(1, 10):
            # 현재 행, 열, 블록에서 num 사용 여부 검사 (O(1) 체크)
            if not rows[i][num] and not cols[j][num] and not blocks[block_index][num]:
                # 후보 num 배치
                board[i][j] = num
                rows[i][num] = True
                cols[j][num] = True
                blocks[block_index][num] = True

                # 다음 빈 칸 채우기 시도
                if backtrack(idx + 1):
                    return True

                # 후보 num이 맞지 않다면, 배치 취소 (백트래킹)
                board[i][j] = 0
                rows[i][num] = False
                cols[j][num] = False
                blocks[block_index][num] = False
        
        # 어떤 숫자도 조건을 만족하지 못했다면 이전 단계로 되돌아감
        return False

    # 스도쿠 해를 찾는다. (여기서는 해가 반드시 존재한다고 가정)
    backtrack(0)
    return board

sudocu = [list(map(int, input().split())) for _ in range(9)]
solved_board = solve_sudoku(sudocu)
for row in solved_board:
    print(*row)
