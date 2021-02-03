n,m = map(int,input().split())
grid = [list(map(int,input().split()))for i in range(n)]
answer = 0



for i in range(n):
    count = 1
    mark = 0
    if n==1:
        answer += 1
        break
    for j in range(1,n):


        if grid[i][j] == grid[i][j-1]:
            count+=1
        else:
            if mark == 0 and count >= m:
                mark = 1
                answer += 1
    if mark == 0 and count >= m:
        answer += 1


        
        
for j in range(n):
    count = 1
    mark = 0
    if n == 1:
        answer += 1
        break
    for i in range(1,n):
        if grid[i][j] == grid[i-1][j]:
            count+=1
        else:
            if mark == 0 and count>=m:
                mark = 1
                answer += 1
    if mark == 0 and count >= m:
        answer += 1


print(answer) 
