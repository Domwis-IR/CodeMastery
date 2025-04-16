def __main__():
    table_length, farthest_length = map(int, input().split())
    hamburger_line = list(input())
    max_people = 0
    for i, ch in enumerate(hamburger_line):
        if ch == "H":
            min_idx_person = len(hamburger_line)
            can_eat = False
            for j in range(farthest_length, -(farthest_length + 1), -1):
                if 0 <= i + j < len(hamburger_line) and hamburger_line[i+j] == "P":
                    min_idx_person = min(min_idx_person, i+j)
                    can_eat = True
            if can_eat:
                max_people += 1
                hamburger_line[i] = "X"
                hamburger_line[min_idx_person] = "X"
    
    print(max_people)


if __name__ == "__main__":
    __main__()