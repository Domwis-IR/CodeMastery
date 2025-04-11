arr = input().split('-') 
s = 0 
for i in arr[0].split('+'): 
    s += int(i) 
for i in arr[1:]: 
    for j in i.split('+'): 
        s -= int(j) 
print(s)

# eval() 함수의 경우 string의 계산식을 한번에 계산을 진행해주나 eval('09')와 같이 0으로 시작하는 숫자의 경우 error가 난다.
# 이를 int()를 이용해서 해결해줄수는 있으나 위와 같이 split으로 해결해주는 것이 식이 더 간단하다.
