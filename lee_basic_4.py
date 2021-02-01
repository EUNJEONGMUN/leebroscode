n,m = map(int,input().split())

grid = [[0 for _ in range(m)] for _ in range(n)]
x,y = 0,0
num = 0
while x<n and y<m:
    grid[x][y] = num
    
    if y % 2 == 0:
        if x == n-1:
            y += 1
        else:
            x += 1
    else: 
        if x == 0:
            y += 1
        else:
            x -= 1
    num += 1

for elem in grid:
    for i in range(len(elem)):
        print(elem[i], end = ' ')
    print()
