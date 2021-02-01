n = int(input())
work = []
for _ in range(n):
    work.append(tuple(map(int,input().split())))

dp =[]
workfinish = 0

for i in range(n):
    money = work[i][2]
    workfinish = work[i][1]
    for j in range(i+1,n):
        if workfinish<work[j][0]:
            workfinish = work[j][1]
            money += work[j][2]
    dp.append(money)

if dp:
    print(max(dp))
else:
    print(0)
    
