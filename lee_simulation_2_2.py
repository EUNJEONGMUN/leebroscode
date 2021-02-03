n,t = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(3)]

for _ in range(t):
    temp1 = grid[0][-1:]
    temp2 = grid[1][-1:]
    temp3 = grid[2][-1:]

    grid[0] = temp3+grid[0][:-1]
    grid[1] = temp1+grid[1][:-1]
    grid[2] = temp2+grid[2][:-1]

for elem in grid:
    for i in range(n):
        print(elem[i], end=' ')
    print()
        
