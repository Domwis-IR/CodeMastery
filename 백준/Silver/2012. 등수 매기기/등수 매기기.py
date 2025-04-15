def main():
    import sys
    input = sys.stdin.readline  # 빠른 입력 처리를 위해 사용
    N = int(input())
    
    # 모든 예상 등수를 하나의 리스트에 저장
    predictions = [int(input()) for _ in range(N)]
    
    # 오름차순 정렬: 가장 작은 예측과 실제 등수 1, 2, … 를 매칭하면 최소 총 불만도가 나온다.
    predictions.sort()
    
    total_dissatisfaction = 0
    # 0부터 N-1까지 반복하며, 실제 등수는 i+1
    for i in range(N):
        total_dissatisfaction += abs(predictions[i] - (i + 1))
    
    print(total_dissatisfaction)

if __name__ == "__main__":
    main()
