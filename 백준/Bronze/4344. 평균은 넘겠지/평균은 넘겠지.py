c = int(input())
for _ in range(c):
    l = list(map(int,input().split()))
    avg = 0
    for num in l[1:]:
        avg += num
    avg = avg // l[0]
    n = 0
    for num in l[1:]:
        if num > avg:
            n += 1
    answer = (n / l[0]) * 100
    print(f'{answer:0.3f}%') # 출력 형식을 기억할 것. 소수점 자릿수 배정은 format으로 가능 not round 함수..
