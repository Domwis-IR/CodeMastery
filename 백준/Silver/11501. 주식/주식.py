import sys

# 테스트 케이스가 많을 경우 sys.stdin.readline()을 사용하는 것이 빠릅니다.
test_cases = int(sys.stdin.readline())

for t in range(test_cases):
    N = int(sys.stdin.readline())
    price_list = list(map(int, sys.stdin.readline().split()))
    
    answer = 0
    max_price = 0  # 현재까지의 최고 주가 (뒤에서부터 탐색 기준)
    
    # 리스트를 뒤에서부터(N-1번째 인덱스부터 0번째 인덱스까지) 순회합니다.
    for i in range(N - 1, -1, -1):
        current_price = price_list[i]
        
        # 1. 현재 가격이 여태껏 본 최고가보다 비싼 경우
        if current_price > max_price:
            # 이 날은 파는 날이 되어야 하므로, max_price를 갱신합니다.
            max_price = current_price
        # 2. 현재 가격이 최고가보다 싼 경우
        else:
            # 이 날 주식을 사서, 이전에 찾은 max_price 날에 팔면 이익입니다.
            # (어차피 그 max_price는 현재 날짜보다 뒤에 있는 날이므로)
            answer += max_price - current_price
            
    print(answer)