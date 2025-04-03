n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]
l = sorted(l, key = lambda x:(x[1],x[0]))
cnt = 0
end = 0
for start, end_ in l:
    if start >= end:
        cnt += 1
        end = end_
print(cnt)