n,m = map(int,input().split())
grid = [list(map(int,input().split()))for i in range(n)]
answer = 0
for i in range(n):
    count = 1
    for j in range(n-1):
        if grid[i][j] == grid[i][j+1]:
            count+=1
        else:
            count = 1
    if count >= m:
        answer += 1
        
        
for j in range(n):
    count = 1
    for i in range(n-1):
        if grid[i][j] == grid[i+1][j]:
            count+=1
        else:
            count = 1
    if count >= m:
        answer += 1


print(answer)
