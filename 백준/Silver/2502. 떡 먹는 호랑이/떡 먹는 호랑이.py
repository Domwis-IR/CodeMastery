day, count = map(int, input().split())
dp = [0] * (day + 1)
dp[day] = count
dp[1] = "a"
dp[2] = "b"
for i in range(3, day + 1):
    dp[i] = dp[i-1] + dp[i-2]

a_cnt = dp[day].count("a")
b_cnt = dp[day].count("b")

a = 1
b = 1
while True:
    if (count - a * a_cnt) % b_cnt == 0:
        b = (count - a * a_cnt) // b_cnt
        break
    else:
        a += 1

print(a)
print(b)