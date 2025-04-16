def __main__():
    table_length, farthest_length = map(int, input().split())
    hamburger_line = list(input())
    max_people = 0

    for i, ch in enumerate(hamburger_line):
        if ch == "P":
            # 사람이면 왼쪽부터 가까운 햄버거를 찾음
            for j in range(i - farthest_length, i + farthest_length + 1):
                if 0 <= j < table_length and hamburger_line[j] == "H":
                    hamburger_line[j] = "X"  # 햄버거 먹음
                    max_people += 1
                    break

    print(max_people)


if __name__ == "__main__":
    __main__()
