n,m = map(int,input().split())
x,y,d = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
visited = [['F' for _ in range(m)] for _ in range(n)]
def InRange(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False
    
def CanGo(x,y):
    if not InRange(x,y):
        return False

    if visited[x][y] == 'T' or arr[x][y] == 1:
        return False
    return True

def DFS(x,y,d):
    if d == 0:
        dx = [0,1,0,-1]
        dy = [-1,0,1,0]
    elif d == 1:
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
    elif d == 2:
        dx = [0,-1,0,1]
        dy = [1,0,-1,0]
    else:
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
    d = (d+1)%4
    


    for i in range(4):
        new_x, new_y = x+dx[i], y+dy[i]

        if CanGo(new_x, new_y):
            visited[new_x][new_y] = 'T'
            DFS(new_x, new_y,d)
        else:
            d = (d+1)%4


visited[x][y] = 'T'
DFS(x,y,d)

num = 0
for i in range(1,n-1):
    for j in range(1,m-1):
        if visited[i][j] == 'T':
            num += 1
print(num)
