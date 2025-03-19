import sys

def char_to_index(ch):
    """
    문자를 0~51의 인덱스로 변환합니다.
    - 대문자 A-Z: 0 ~ 25
    - 소문자 a-z: 26 ~ 51
    """
    if 'A' <= ch <= 'Z':
        return ord(ch) - ord('A')
    else:
        return ord(ch) - ord('a') + 26

def compute_pattern_count(W):
    """
    단어 W의 각 문자가 등장하는 빈도를 계산하여 배열로 반환합니다.
    """
    pattern_count = [0] * 52
    for ch in W:
        pattern_count[char_to_index(ch)] += 1
    return pattern_count

def compute_initial_diff(S, g, pattern_count):
    """
    S의 첫 윈도우(길이 g)에 대해 diff 배열을 계산합니다.
    diff[i] = (윈도우 내 문자의 등장 빈도수) - (W의 등장 빈도수)
    """
    diff = [0] * 52
    for i in range(g):
        diff[char_to_index(S[i])] += 1
    for i in range(52):
        diff[i] -= pattern_count[i]
    return diff

def update_char(diff, matches, idx, delta):
    """
    diff 배열의 idx 위치 값을 delta만큼 업데이트하면서,
    해당 인덱스의 값이 0인 경우(matches)를 적절히 조정합니다.
    """
    if diff[idx] == 0:
        matches -= 1
    diff[idx] += delta
    if diff[idx] == 0:
        matches += 1
    return matches

def count_permutation_occurrences(W, S, g, s_len):
    """
    문자열 S 내에서 W의 순열이 부분 문자열로 나타나는 경우의 수를 계산합니다.
    """
    pattern_count = compute_pattern_count(W)
    diff = compute_initial_diff(S, g, pattern_count)
    
    # diff 배열의 각 인덱스 값이 0인 개수를 matches에 저장
    matches = sum(1 for i in range(52) if diff[i] == 0)
    
    count = 0
    if matches == 52:
        count += 1

    # 슬라이딩 윈도우 기법 적용
    for i in range(g, s_len):
        out_idx = char_to_index(S[i - g])  # 윈도우에서 빠지는 문자
        in_idx = char_to_index(S[i])         # 새로 들어오는 문자

        matches = update_char(diff, matches, out_idx, -1)
        matches = update_char(diff, matches, in_idx, 1)

        if matches == 52:
            count += 1

    return count

def main():
    g, s = map(int, input().split())
    W = input().strip()
    S = input().strip()


    result = count_permutation_occurrences(W, S, g, s)
    print(result)

if __name__ == '__main__':
    main()
