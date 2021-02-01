n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
visited = [['F' for _ in range(m)] for _ in range(n)]



def InRange(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False
    
def CanGo(x,y):
    if not InRange(x,y):
        return False
    if (visited[x][y] == 'T') or (arr[x][y]==0):
        return False
    return True

def DFS(x,y):
    dx = [1,0]
    dy = [0,1]

    for i in range(2):
        new_x, new_y = x+dx[i], y+dy[i]

        if(CanGo(new_x,new_y)):
            visited[new_x][new_y] = 'T'
            DFS(new_x,new_y)


visited[0][0] = 'T'
DFS(0,0)

if visited[n-1][m-1] == 'T':
    print(1)
else:
    print(0)
